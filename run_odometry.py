import os
import argparse
from pathlib import Path
import yaml
from easydict import EasyDict as edict
import torch
from torchvision import transforms
import numpy as np
from PIL import Image
from tqdm import tqdm

from models import create_posenet_early, create_posenet_late, create_posenet_middle, create_posenet_multi_layer
from libs.kinetics import from_euler_t
from libs.misc import create_dir_if_not_exist
from modules.monodepth2.networks import ResnetEncoder
from modules.monodepth2.networks import DepthDecoder


posenet_type_dict = {
    'early': create_posenet_early,
    'late': create_posenet_late,
    'middle': create_posenet_middle,
    'multi_layer': create_posenet_multi_layer
}


def pil_loader(path):
    # open path as file to avoid ResourceWarning
    # (https://github.com/python-pillow/Pillow/issues/835)
    with open(path, 'rb') as f:
        with Image.open(f) as img:
            return img.convert('RGB')


class KIITIOdomDataset:
    def __init__(self, config_dict) -> None:
        super().__init__()

        self.seq_dir = os.path.join(config_dict.data.path, 'image_2')
        self.height = config_dict.data.height
        self.width = config_dict.data.width

        self.filename_list = sorted(os.listdir(self.seq_dir))
        self.loader = pil_loader
        self.resize = transforms.Resize((self.height, self.width), interpolation=Image.ANTIALIAS)
        self.to_tensor = transforms.ToTensor()

    def __len__(self):
        return len(self.filename_list)

    def preprocess(self, rgb_image):
        rgb_image = self.to_tensor(self.resize(rgb_image))
        return rgb_image[None, ...].cuda()

    def getitem(self, index):
        filename = self.filename_list[index]
        file_path = os.path.join(self.seq_dir, filename)
        rgb_image = self.loader(file_path)
        rgb_image = self.preprocess(rgb_image)

        return rgb_image


