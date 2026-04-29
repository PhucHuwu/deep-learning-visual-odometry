# deep-learning-visual-odometry

Monocular visual odometry with RGB and predicted-disparity fusion.

## Team

- Phuc TranHuu: [PhucHuwu](https://github.com/PhucHuwu)
- Khoi NguyenVuTuan: [nvtuankhoi](https://github.com/nvtuankhoi)

## Method

Consecutive monocular RGB images provide the input.
Monodepth2 predicts disparity from RGB; this is not independent depth-sensor input.
Relative motion predictions are accumulated into a camera trajectory.
The PoseNet variants are early, middle, late, and multi-layer fusion.

## Pipeline

Images are resized to 192 by 640, converted to tensors, and passed to the depth encoder and decoder. Consecutive RGB and repeated disparity tensors form the two PoseNet inputs. Predicted motion is converted into an inverted relative transform and accumulated.

## Structure

`models/` contains fusion architectures; `libs/` contains geometry helpers; `configs/` contains inference settings; `run_odometry.py` runs sequence inference.

## Environment

The requirements pin PyTorch 1.7.1 with CUDA 10.1 and torchvision 0.8.2. Use a Python version supported by that legacy stack. The inference script requires CUDA.

```bash
python -m pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html
```

Pillow and tqdm are also required. The legacy resize API needs Pillow before version 10. These installation instructions are not a verified environment.

Upstream dependencies are Git submodules. Initialize them with `git submodule update --init --recursive`.

## Data

The default sequence is `data/dataset/sequences/09/image_2/`, containing ordered RGB images. Dataset files are not included.

The checkpoint directory must contain `encoder.pth`, `depth.pth`, and an architecture-compatible `pose.pth`. Weights are not included.

Select the input path, resize dimensions, model path, fusion type, and output directory in `configs/run_odometry.yaml`.
