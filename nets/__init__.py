from .mobilenetv2 import mobilenetv2
from .resnet import resnet18, resnet34, resnet50, resnet101, resnet152
from .vgg import vgg11, vgg13, vgg16, vgg11_bn, vgg13_bn, vgg16_bn
from .vision_transformer import vit_b_16
from .swin_transformer import swin_transformer_base, swin_transformer_small, swin_transformer_tiny,swin_transformer_base_384
from .swin_transformer_v2 import swin_transformerv2

from .densenet import densenet121,densenet169,densenet201
from .shufflenetv2 import shufflenet_v2_x0_5
from .convnext import convnext_base
from .efficientnet import EfficientNetModel
from .inceptionv4 import inceptionv4
get_model_from_name = {
    "mobilenetv2"               : mobilenetv2,
    "resnet18"                  : resnet18,
    "resnet34"                  : resnet34,
    "resnet50"                  : resnet50,
    "resnet101"                 : resnet101,
    "resnet152"                 : resnet152,
    "vgg11"                     : vgg11,
    "vgg13"                     : vgg13,
    "vgg16"                     : vgg16,
    "vgg11_bn"                  : vgg11_bn,
    "vgg13_bn"                  : vgg13_bn,
    "vgg16_bn"                  : vgg16_bn,
    "vit_b_16"                  : vit_b_16,
    "swin_transformer_tiny"     : swin_transformer_tiny,
    "swin_transformer_small"    : swin_transformer_small,
    "swin_transformer_base"     : swin_transformer_base,
    "swin_transformer_base_384" : swin_transformer_base_384,
    "swin_transformerv2"        : swin_transformerv2,

    "densenet121"               : densenet121,
    "densenet169"               : densenet169,
    "densenet201"               : densenet201,
    "convnext"                  : convnext_base,
    "efficientnet"              : EfficientNetModel,
    "inceptionv4"               : inceptionv4,

}