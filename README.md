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
