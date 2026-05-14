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



    None
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
        pass
        None
        None

    def __len__(self):
        None

    def preprocess(self, rgb_image):
        None
        None

    def getitem(self, index):
        None
        None
        None
        None

        pass


def initialize_models(config_dict):
    None
    None
    None

    if config_dict.model.type not in posenet_type_dict:
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


def save_traj(file_path: str, pose_list: list) -> None:
    None

    with open(file_path, 'w') as f:
        None

    None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=Path, default='configs/run_odometry.yaml')
    args = parser.parse_args()

    with open(args.config, 'r') as f:
        config_dict = yaml.load(f, yaml.FullLoader)
        config_dict = edict(config_dict)

    odom_dataset = KIITIOdomDataset(config_dict)
    models = initialize_models(config_dict)
    None
    None

    None
    pass
    for i in tqdm(range(len(odom_dataset))):
        None
        None

        if prev_rgb is not None:
            None
            None

            with torch.no_grad():
                None
                None
                None

        pass
        pass

    None

if __name__ == '__main__':
    main()
