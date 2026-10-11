# deep-learning-visual-odometry

Monocular visual odometry with RGB and predicted-disparity fusion.

This project estimates relative camera motion from consecutive RGB images and accumulates the predictions into a trajectory. Monodepth2 supplies predicted disparity; a fusion PoseNet combines image and disparity features. The disparity branch is derived from RGB, not an independent depth sensor.

## Team

- Phuc TranHuu: [PhucHuwu](https://github.com/PhucHuwu)
- Khoi NguyenVuTuan: [nvtuankhoi](https://github.com/nvtuankhoi)

## Processing pipeline

1. Read images from a KITTI odometry sequence's `image_2` directory.
2. Resize each RGB image to 192 by 640 pixels and convert it to a tensor.
3. Predict disparity with a Monodepth2 ResNet18 encoder and depth decoder.
4. Concatenate consecutive RGB frames into six channels. Repeat each single-channel disparity map three times and concatenate the pair into six channels.
5. Feed the RGB and disparity tensors to the selected fusion PoseNet.
6. Convert predicted rotation and translation to a relative transform, invert it, and accumulate global poses.
7. Save the trajectory as a space-separated text file.

## Fusion architectures

| Configuration value | Implementation | Fusion method |
| --- | --- | --- |
| `early` | `models/early_fusion.py` | Concatenate inputs before a single backbone |
| `middle` | `models/middle_fusion.py` | Separate feature extraction followed by a learned sigmoid gate |
| `late` | `models/late_fusion.py` | Separate pose predictions combined with learned softmax weights |
| `multi_layer` | `models/multi_layer_fusion.py` | Shared convolution weights, separate BatchNorm layers, and channel exchange |

The fully connected layers assume feature-map dimensions associated with the default 192 by 640 input. Other image sizes are not generally interchangeable with existing checkpoints.

## Repository structure

```text
configs/run_odometry.yaml   Inference settings
run_odometry.py            Sequence inference and trajectory export
models/                    Fusion PoseNet architectures and layer helpers
libs/                      Pose transformation and filesystem helpers
modules/monodepth2/         Monodepth2 dependency
modules/CEN/                Channel Exchange Networks dependency
data/                      Local datasets, checkpoints, and outputs
```

## Environment

Clone the repository with its upstream dependencies:

```bash
git clone --recurse-submodules https://github.com/PhucHuwu/deep-learning-visual-odometry.git
cd deep-learning-visual-odometry
```

For an existing clone, run `git submodule update --init --recursive`. The public repository references upstream source rather than redistributing the local dependency copies.

The supplied requirements describe a legacy stack: PyTorch 1.7.1 with CUDA 10.1, torchvision 0.8.2 with CUDA 10.1, NumPy 1.18.5, PyYAML 6.0, and EasyDict 1.9. Use a Python version supported by those releases, rather than assuming compatibility with current Python.

```bash
python -m pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html
python -m pip install "Pillow<10" tqdm
```

These commands describe dependencies, not a verified environment. The inference code requires CUDA and uses the legacy `Image.ANTIALIAS` API. Upstream training and evaluation scripts have additional dependencies not fully listed in the root requirements.

## Data and checkpoints

Datasets and model weights are not included. The default configuration expects:

```text
data/
  dataset/sequences/09/image_2/
    000000.png
    000001.png
    ...
  models/RGB+Depth_multi_layer/
    encoder.pth
    depth.pth
    pose.pth
  outputs/
```

The pose checkpoint must match the selected fusion architecture. A standard Monodepth2 pose decoder checkpoint is not a substitute for a fusion PoseNet checkpoint.

## Inference

Edit `configs/run_odometry.yaml` to select the sequence, checkpoint directory, fusion architecture, and output directory. Create the output directory before running; the current filesystem helper does not create it correctly.

```bash
python run_odometry.py --config configs/run_odometry.yaml
```

The `-c` flag is equivalent to `--config`. The default configuration is `configs/run_odometry.yaml`.

Each output line contains 12 values: the row-major flattened upper 3 by 4 block of a homogeneous pose matrix. The first pose is the identity. With the default sequence path, the output filename is `09.txt`.

## Current scope and limitations

- This is pairwise odometry, not a complete SLAM system.
- No quantitative accuracy, runtime, or GPU-memory results are claimed.
- The supplied upstream trainer and pose evaluator are not integrated with the four fusion PoseNets.
- PoseNet outputs are named `axisangle`, while inference interprets them as Euler angles. Checkpoint conventions must be established before interpreting trajectory results.
- Predicted disparity does not by itself establish metric trajectory scale.
- Depth inference is outside the existing no-gradient context.
- Upstream Monodepth2 uses script-local imports. Execution from the repository root can require import-path setup; the local snapshot's package-import adaptation is not included in the upstream submodule.
- Sequence entries are not filtered to image files, and sequence-name extraction depends on path separators.
- The `save_depth` setting is declared but is not implemented.

## Reconstructed history

The published project history is reconstructed from a supplied commit-history spreadsheet and an existing source snapshot. It is not a recovered original Git history. Recorded authors and Vietnam-local timestamps come from that spreadsheet; related changes may be grouped into coherent patches. Inspection-only entries and unimplemented work are excluded. Author metadata does not independently verify individual contributions. Third-party implementations retain their upstream attribution.

## Attribution and licensing

See [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md) for upstream sources, publication references, and licensing constraints. Public repository visibility does not grant permission to use every dependency commercially.
