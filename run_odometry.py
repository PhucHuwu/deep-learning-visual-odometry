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


