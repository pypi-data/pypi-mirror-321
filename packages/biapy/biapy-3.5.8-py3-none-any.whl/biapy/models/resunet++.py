import torch
import torch.nn as nn
from typing import List

from biapy.models.blocks import (
    ResConvBlock,
    ResUpBlock,
    SqExBlock,
    ASPP,
    ResUNetPlusPlus_AttentionBlock,
)


class ResUNetPlusPlus(nn.Module):
    """
    Create 2D/3D ResUNet++.

    Reference: `ResUNet++: An Advanced Architecture for Medical Image Segmentation <https://arxiv.org/pdf/1911.07067.pdf>`_.

    Parameters
    ----------
    image_shape : 3D/4D tuple
        Dimensions of the input image. E.g. ``(y, x, channels)`` or ``(z, y, x, channels)``.

    activation : str, optional
        Activation layer.

    feature_maps : array of ints, optional
        Feature maps to use on each level.

    drop_values : float, optional
        Dropout value to be fixed.

    normalization : str, optional
        Normalization layer (one of ``'bn'``, ``'sync_bn'`` ``'in'``, ``'gn'`` or ``'none'``).

    k_size : int, optional
        Kernel size.

    upsample_layer : str, optional
        Type of layer to use to make upsampling. Two options: "convtranspose" or "upsampling".

    z_down : List of ints, optional
        Downsampling used in z dimension. Set it to ``1`` if the dataset is not isotropic.

    n_classes: int, optional
        Number of classes.

    output_channels : str, optional
        Channels to operate with. Possible values: ``BC``, ``BCD``, ``BP``, ``BCDv2``,
        ``BDv2``, ``Dv2`` and ``BCM``.

    upsampling_factor : tuple of ints, optional
        Factor of upsampling for super resolution workflow for each dimension.

    upsampling_position : str, optional
        Whether the upsampling is going to be made previously (``pre`` option) to the model
        or after the model (``post`` option).

    Returns
    -------
    model : Torch model
        ResUNet++ model.


    Calling this function with its default parameters returns the following network:

    .. image:: ../../img/models/unet.png
        :width: 100%
        :align: center

    Image created with `PlotNeuralNet <https://github.com/HarisIqbal88/PlotNeuralNet>`_.
    """

    def __init__(
        self,
        image_shape=(256, 256, 1),
        activation="ELU",
        feature_maps=[32, 64, 128, 256],
        drop_values=[0.1, 0.1, 0.1, 0.1],
        normalization="none",
        k_size=3,
        upsample_layer="convtranspose",
        z_down=[2, 2, 2, 2],
        n_classes=1,
        output_channels="BC",
        upsampling_factor=(),
        upsampling_position="pre",
    ):
        super(ResUNetPlusPlus, self).__init__()

        self.depth = len(feature_maps) - 2
        self.ndim = 3 if len(image_shape) == 4 else 2
        self.z_down = z_down
        self.n_classes = 1 if n_classes <= 2 else n_classes
        self.multiclass = True if n_classes > 2 and output_channels is not None else False
        if self.ndim == 3:
            conv = nn.Conv3d
            convtranspose = nn.ConvTranspose3d
            pooling = nn.MaxPool3d
        else:
            conv = nn.Conv2d
            convtranspose = nn.ConvTranspose2d
            pooling = nn.MaxPool2d

        # Super-resolution
        self.pre_upsampling = None
        if len(upsampling_factor) > 1 and upsampling_position == "pre":
            self.pre_upsampling = convtranspose(
                image_shape[-1],
                image_shape[-1],
                kernel_size=upsampling_factor,
                stride=upsampling_factor,
            )

        # ENCODER
        self.down_path = nn.ModuleList()
        self.mpooling_layers = nn.ModuleList()
        self.sqex_blocks = nn.ModuleList()
        self.down_path.append(
            ResConvBlock(
                conv=conv,
                in_size=image_shape[-1],
                out_size=feature_maps[0],
                k_size=k_size,
                act=activation,
                norm=normalization,
                dropout=drop_values[0],
                skip_k_size=k_size,
                skip_norm=normalization,
                first_block=True,
            )
        )
        self.sqex_blocks.append(SqExBlock(feature_maps[0], ndim=self.ndim))
        mpool = (z_down[0], 2, 2) if self.ndim == 3 else (2, 2)
        self.mpooling_layers.append(pooling(mpool))
        in_channels = feature_maps[0]
        for i in range(self.depth):
            self.down_path.append(
                ResConvBlock(
                    conv=conv,
                    in_size=in_channels,
                    out_size=feature_maps[i + 1],
                    k_size=k_size,
                    act=activation,
                    norm=normalization,
                    dropout=drop_values[i],
                    skip_k_size=k_size,
                    skip_norm=normalization,
                    first_block=False,
                )
            )
            mpool = (z_down[i + 1], 2, 2) if self.ndim == 3 else (2, 2)
            self.mpooling_layers.append(pooling(mpool))
            in_channels = feature_maps[i + 1]
            if i != self.depth - 1:
                self.sqex_blocks.append(SqExBlock(in_channels, ndim=self.ndim))
        self.sqex_blocks.append(
            None
        )  # So it can be used zip() with the length of self.down_path and self.mpooling_layers
        self.aspp_bridge = ASPP(
            conv=conv,
            in_dims=in_channels,
            out_dims=feature_maps[-1],
            norm=normalization,
        )

        # DECODER
        self.up_path = nn.ModuleList()
        self.attentions = nn.ModuleList()
        for i in range(self.depth - 1, -1, -1):
            self.attentions.append(
                ResUNetPlusPlus_AttentionBlock(
                    conv=conv,
                    maxpool=pooling,
                    input_encoder=feature_maps[i],
                    input_decoder=feature_maps[i + 2],
                    output_dim=feature_maps[i + 2],
                    norm=normalization,
                    z_down=z_down[i + 1],
                )
            )
            self.up_path.append(
                ResUpBlock(
                    ndim=self.ndim,
                    convtranspose=convtranspose,
                    in_size=feature_maps[i + 2],
                    out_size=feature_maps[i + 1],
                    in_size_bridge=feature_maps[i],
                    z_down=z_down[i + 1],
                    up_mode=upsample_layer,
                    conv=conv,
                    k_size=k_size,
                    act=activation,
                    norm=normalization,
                    dropout=drop_values[i + 2],
                    skip_k_size=k_size,
                    skip_norm=normalization,
                )
            )
        self.aspp_out = ASPP(
            conv=conv,
            in_dims=feature_maps[1],
            out_dims=feature_maps[0],
            norm=normalization,
        )

        # Super-resolution
        self.post_upsampling = None
        if len(upsampling_factor) > 1 and upsampling_position == "post":
            self.post_upsampling = convtranspose(
                feature_maps[0],
                feature_maps[0],
                kernel_size=upsampling_factor,
                stride=upsampling_factor,
            )

        # Instance segmentation
        if output_channels is not None:
            if output_channels in ["C", "Dv2"]:
                self.last_block = conv(feature_maps[0], 1, kernel_size=1, padding="same")
            elif output_channels in ["BC", "BP"]:
                self.last_block = conv(feature_maps[0], 2, kernel_size=1, padding="same")
            elif output_channels in ["BDv2", "BD"]:
                self.last_block = conv(feature_maps[0], 2, kernel_size=1, padding="same")
            elif output_channels in ["BCM", "BCD", "BCDv2"]:
                self.last_block = conv(feature_maps[0], 3, kernel_size=1, padding="same")
            elif output_channels in ["A"]:
                self.last_block = conv(feature_maps[0], self.ndim, kernel_size=1, padding="same")
        # Other
        else:
            self.last_block = conv(feature_maps[0], self.n_classes, kernel_size=1, padding="same")

        # Multi-head: instances + classification
        self.last_class_head = None
        if self.multiclass:
            self.last_class_head = conv(feature_maps[0], self.n_classes, kernel_size=1, padding="same")

        self.apply(self._init_weights)

    def forward(self, x) -> torch.Tensor | List[torch.Tensor]:
        # Super-resolution
        if self.pre_upsampling is not None:
            x = self.pre_upsampling(x)

        # Down
        blocks = []
        for i, layers in enumerate(zip(self.down_path, self.sqex_blocks, self.mpooling_layers)):
            down, sqex, pool = layers
            x = down(x)
            if i < len(self.down_path) - 1:  # Avoid last block
                x = sqex(x)
            if i != len(self.down_path):
                if i != 0:  # First level is not downsampled
                    x = pool(x)
                blocks.append(x)

        x = self.aspp_bridge(x)

        # Up
        for i, layers in enumerate(zip(self.attentions, self.up_path)):
            att, up = layers
            x = att(blocks[-i - 2], x)
            x = up(x, blocks[-i - 2])

        x = self.aspp_out(x)

        # Super-resolution
        if self.post_upsampling is not None:
            x = self.post_upsampling(x)

        class_head_out = torch.empty(())
        if self.multiclass and self.last_class_head is not None:
            class_head_out = self.last_class_head(x)

        x = self.last_block(x)

        if self.multiclass:
            return [x, class_head_out]
        else:
            return x

    def _init_weights(self, m):
        if isinstance(m, nn.Conv2d) or isinstance(m, nn.Conv3d):
            nn.init.xavier_uniform_(m.weight)
            if m.bias is not None:
                nn.init.constant_(m.bias, 0)
        elif isinstance(m, nn.Linear):
            nn.init.xavier_uniform_(m.weight)
            if isinstance(m, nn.Linear) and m.bias is not None:
                nn.init.constant_(m.bias, 0)
        elif isinstance(m, nn.LayerNorm):
            nn.init.constant_(m.bias, 0)
            nn.init.constant_(m.weight, 1.0)
