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
