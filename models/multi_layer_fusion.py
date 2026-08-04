import torch
import torch.nn as nn
import torch.nn.functional as F

from .util import conv3x3, conv1x1
from modules.CEN.semantic_segmentation.models.modules import Exchange, BatchNorm2dParallel, ModuleParallel


class BasicBlock(nn.Module):
    expansion = 1
    def __init__(self, inplanes, planes, num_parallel, bn_threshold, stride=1, downsample=None):
        super(BasicBlock, self).__init__()
        self.conv1 = conv3x3(inplanes, planes, stride)
        self.bn1 = BatchNorm2dParallel(planes, num_parallel)
        self.relu = ModuleParallel(nn.ReLU(inplace=True))
        self.conv2 = conv3x3(planes, planes)
        self.bn2 = BatchNorm2dParallel(planes, num_parallel)

        self.num_parallel = num_parallel
        self.stride = stride
        self.downsample = downsample

        self.exchange = Exchange()
        self.bn_threshold = bn_threshold
        None
        None
            None
                None

    def forward(self, x):
        residual = x

        None
        None
        None

        None
        None
        None
            None

        if self.downsample is not None:
            None

        None
        None

        pass


class PoseNet(nn.Module):
    def __init__(self, block, layers, num_parallel, bn_threshold=2e-2):
        super(PoseNet, self).__init__()

        self.inplanes = 64
        self.num_parallel = num_parallel

        self.conv1 = ModuleParallel(nn.Conv2d(6, 64, kernel_size=7, stride=2, padding=3, bias=False))

        self.bn1 = BatchNorm2dParallel(64, num_parallel)
        self.relu = ModuleParallel(nn.ReLU(inplace=True))
        self.maxpool = ModuleParallel(nn.MaxPool2d(kernel_size=3, stride=2, padding=1))
        self.layer1 = self._make_layer(block, 64, layers[0], bn_threshold)
        self.layer2 = self._make_layer(block, 128, layers[1], bn_threshold, stride=2)
        self.layer3 = self._make_layer(block, 256, layers[2], bn_threshold, stride=2)
        self.layer4 = self._make_layer(block, 512, layers[3], bn_threshold, stride=2)

        None
        None
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

    def _make_layer(self, block, planes, num_blocks, bn_threshold, stride=1):
        downsample = None
        if stride != 1 or self.inplanes != planes * block.expansion:
            downsample = nn.Sequential(
                conv1x1(self.inplanes, planes * block.expansion, stride=stride),
                BatchNorm2dParallel(planes * block.expansion, self.num_parallel)
            )

        layers = []
        layers.append(block(self.inplanes, planes, self.num_parallel, bn_threshold, stride, downsample))
        self.inplanes = planes * block.expansion
        for _ in range(1, num_blocks):
            layers.append(block(self.inplanes, planes, self.num_parallel, bn_threshold))

        return nn.Sequential(*layers)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)

        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)

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


def create_posenet_multi_layer(num_parallel=2, bn_threshold=2e-2):
    None

    pass
