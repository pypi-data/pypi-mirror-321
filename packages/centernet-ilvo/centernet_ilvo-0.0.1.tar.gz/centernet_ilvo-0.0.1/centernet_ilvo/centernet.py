import torch
import torch.nn as nn
import torchvision
from torchvision.models import (ResNet34_Weights, ResNet18_Weights, ResNet50_Weights,
                                ResNet101_Weights, EfficientNet_B4_Weights,
                                EfficientNet_V2_S_Weights, EfficientNet_V2_M_Weights, EfficientNet_V2_L_Weights)
import torch.nn.functional as F
from enum import Enum


class BackboneModels(str, Enum):
    RESNET18 = "resnet18"
    RESNET34 = "resnet34"
    RESNET50 = "resnet50"
    RESNET101 = "resnet101"
    EFFICIENTNET_B4 = "efficientnet_b4"
    EFFICIENTNET_V2_S = "efficientnet_v2_s"
    EFFICIENTNET_V2_M = "efficientnet_v2_m"


# From centernet repo
def neg_loss(pred, gt):
    """
    Modified focal loss. Exactly the same as CornerNet.
    Runs faster and costs a little bit more memory
    """
    pred = pred.unsqueeze(1).float()
    gt = gt.unsqueeze(1).float()

    pos_inds = gt.eq(1).float()
    neg_inds = gt.lt(1).float()
    neg_weights = torch.pow(1 - gt, 4)

    loss = 0

    pos_loss = torch.log(pred + 1e-12) * torch.pow(1 - pred, 3) * pos_inds  # 3 is a hyper parameter
    neg_loss = torch.log(1 - pred + 1e-12) * torch.pow(pred, 3) * neg_weights * neg_inds

    num_pos = pos_inds.float().sum()
    pos_loss = pos_loss.sum()
    neg_loss = neg_loss.sum()

    if num_pos == 0:
        loss = loss - neg_loss
    else:
        loss = loss - (pos_loss + neg_loss) / num_pos
    return loss


def centerloss(prediction, mask):
    # Binary mask loss
    pred_mask = torch.sigmoid(prediction[:, 0])
    mask_loss = neg_loss(pred_mask, mask)

    return mask_loss


class double_conv(nn.Module):
    """
    (conv => BN => ReLU) * 2
    """
    def __init__(self, in_ch, out_ch):
        super(double_conv, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        x = self.conv(x)
        return x


class up(nn.Module):
    def __init__(self, in_ch, out_ch, bilinear=True):
        super(up, self).__init__()
        if bilinear:
            self.up = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
        else:
            self.up = nn.ConvTranspose2d(in_ch // 2, in_ch // 2, 2, stride=2)
        self.conv = double_conv(in_ch, out_ch)

    def forward(self, x1, x2=None):
        x1 = self.up(x1)
        if x2 is not None:
            x = torch.cat([x2, x1], dim=1)
            # input is CHW
            diffY = x2.size()[2] - x1.size()[2]
            diffX = x2.size()[3] - x1.size()[3]

            x1 = F.pad(x1, (diffX // 2, diffX - diffX // 2,
                            diffY // 2, diffY - diffY // 2))
        else:
            x = x1
        x = self.conv(x)
        return x


class CenterNet(nn.Module):
    def __init__(self, backbone_model=BackboneModels.RESNET18, pretrained=False, n_classes=1):
        super(CenterNet, self).__init__()
        # create backbone.
        basemodel = None
        self.num_ch = 512
        assert backbone_model in [member.value for member in BackboneModels]

        print("Loading %s as models. %s" % (backbone_model, "(pretrained)" if pretrained else ""))
        if backbone_model == BackboneModels.RESNET18:
            basemodel = torchvision.models.resnet18(weights=ResNet18_Weights.IMAGENET1K_V1) if pretrained else torchvision.models.resnet18()
            self.num_ch = 512
        elif backbone_model == BackboneModels.RESNET34:
            basemodel = torchvision.models.resnet34(weights=ResNet34_Weights.IMAGENET1K_V1) if pretrained else torchvision.models.resnet34()
            self.num_ch = 512
        elif backbone_model == BackboneModels.RESNET50:
            basemodel = torchvision.models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1) if pretrained else torchvision.models.resnet50()
            self.num_ch = 2048
        elif backbone_model == BackboneModels.RESNET101:
            basemodel = torchvision.models.resnet101(weights=ResNet101_Weights.IMAGENET1K_V1) if pretrained else torchvision.models.resnet101()
            self.num_ch = 2048
        elif backbone_model == BackboneModels.EFFICIENTNET_B4:
            basemodel = torchvision.models.efficientnet_b4(weights=EfficientNet_B4_Weights.IMAGENET1K_V1) if pretrained else torchvision.models.efficientnet_b4()
            self.num_ch = 1792
        elif backbone_model == BackboneModels.EFFICIENTNET_V2_S:
            basemodel = torchvision.models.efficientnet_v2_s(weights=EfficientNet_V2_S_Weights.IMAGENET1K_V1) if pretrained else torchvision.models.efficientnet_v2_s()
            self.num_ch = 1280
        elif backbone_model == BackboneModels.EFFICIENTNET_V2_M:
            basemodel = torchvision.models.efficientnet_v2_m(weights=EfficientNet_V2_M_Weights.IMAGENET1K_V1) if pretrained else torchvision.models.efficientnet_v2_m()
            self.num_ch = 1280

        # set basemodel
        basemodel = nn.Sequential(*list(basemodel.children())[:-2])

        self.base_model = basemodel

        self.up1 = up(self.num_ch, 512)
        self.up2 = up(512, 256)
        self.up3 = up(256, 256)
        # output classification
        self.outc = nn.Conv2d(256, n_classes, 1)

    def forward(self, x):
        x = self.base_model(x)

        # Add positional info
        x = self.up1(x)
        x = self.up2(x)
        x = self.up3(x)
        outc = self.outc(x)
        return outc
