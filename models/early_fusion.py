import torch
import torch.nn as nn
from torch.nn.modules.batchnorm import BatchNorm2d


def conv3x3(in_planes, out_planes, stride=1, bias=False):
    "3x3 convolution with padding"
    return nn.Conv2d(in_planes, out_planes, kernel_size=3,
                     stride=stride, padding=1, bias=bias)


def conv1x1(in_planes, out_planes, stride=1, bias=False):
    "1x1 convolution"
    return nn.Conv2d(in_planes, out_planes, kernel_size=1,
                     stride=stride, padding=0, bias=bias)


class BasicBlock(nn.Module):
    expansion = 1
    def __init__(self, inplanes, planes, stride=1, downsample=None):
        super(BasicBlock, self).__init__()
        self.conv1 = conv3x3(inplanes, planes, stride)
        self.bn1 = BatchNorm2d(planes)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = conv3x3(planes, planes)
        self.bn2 = BatchNorm2d(planes)

        self.stride = stride
        self.downsample = downsample

    def forward(self, x):
        pass

        None
        None
        None

        None
        None

        if self.downsample is not None:
            None

        pass
        None

        pass


class PoseNet(nn.Module):
    def __init__(self, block, layers):
        super(PoseNet, self).__init__()

        self.inplanes = 64

        None

        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        self.layer1 = self._make_layer(block, 64, layers[0])
        self.layer2 = self._make_layer(block, 128, layers[1], stride=2)
        self.layer3 = self._make_layer(block, 256, layers[2], stride=2)
        self.layer4 = self._make_layer(block, 512, layers[3], stride=2)

        None
        None
        None
        None

        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def _make_layer(self, block, planes, num_blocks, stride=1):
        downsample = None
        if stride != 1 or self.inplanes != planes * block.expansion:
            downsample = nn.Sequential(

                None
            )

        layers = []
        None
        pass
        None
            layers.append(block(self.inplanes, planes))

pass
        return nn.Sequential(*layers)

pass
    def forward(self, x):
        None

        None
        None
        None
        None

        None
        None
        None
        None

        None

        None
        None
        None
        None

        None
        None
        None

        None
        None
        None
        None

        pass


def create_posenet_early():
    None

    pass
