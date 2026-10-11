# Acknowledgements

This project builds on published depth-estimation and multimodal-fusion implementations. Reconstructed project commit authorship does not imply authorship of third-party code.

## Monodepth2

Source: [nianticlabs/monodepth2](https://github.com/nianticlabs/monodepth2).

The depth encoder, decoder, geometry layers, datasets, and upstream training and evaluation utilities originate from Monodepth2. The public repository references it as an upstream submodule. The local source snapshot contains package-import adaptation in `modules/monodepth2/__init__.py`; that adaptation is not included in the public submodule and is not evidence of an upstream feature.

Publication: **Digging Into Self-Supervised Monocular Depth Estimation**, Clement Godard, Oisin Mac Aodha, Michael Firman, and Gabriel J. Brostow, ICCV 2019. The upstream license specifies acknowledgement of arXiv:1806.01260.

```bibtex
@inproceedings{godard2019digging,
  title={Digging Into Self-Supervised Monocular Depth Estimation},
  author={Godard, Clement and Mac Aodha, Oisin and Firman, Michael and Brostow, Gabriel J.},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  year={2019}
}
```

Copyright Niantic, Inc. 2018. All rights reserved. The [upstream license](https://github.com/nianticlabs/monodepth2/blob/master/LICENSE) limits use to non-commercial purposes and includes redistribution restrictions. Refer to its full text, rather than treating this summary as a license grant.

## Channel Exchange Networks

Source: [yikaiw/CEN](https://github.com/yikaiw/CEN).

The project uses `Exchange`, `ModuleParallel`, and `BatchNorm2dParallel` from the CEN semantic-segmentation implementation. Multi-layer PoseNet adapts those mechanisms to RGB and predicted-disparity fusion for camera-motion estimation.

```bibtex
@inproceedings{wang2020cen,
  title={Deep Multimodal Fusion by Channel Exchanging},
  author={Wang, Yikai and Huang, Wenbing and Sun, Fuchun and Xu, Tingyang and Rong, Yu and Huang, Junzhou},
  booktitle={Advances in Neural Information Processing Systems},
  year={2020}
}
```

The upstream CEN README identifies its license as MIT. Its bundled components also include their own notices, including the RefineNet-LightWeight notice in the semantic-segmentation entry point. Preserve applicable component notices and consult the upstream repository for the full terms.

## KITTI

The default sequence layout follows the [KITTI odometry benchmark](https://www.cvlibs.net/datasets/kitti/eval_odometry.php). KITTI data is not distributed with this project. Obtain it from the dataset provider and follow its usage terms.

## Other implementation references

`libs/kinetics.py` cites the Euler-rotation utilities in [pulkitag/pycaffe-utils](https://github.com/pulkitag/pycaffe-utils/blob/master/rot_utils.py). Other bundled upstream files contain their own implementation references and copyright notices, which must remain attached to their respective code.

## Project licensing status

No blanket MIT or other permissive license is asserted for the whole project. Upstream licenses remain applicable to their respective material. Contact the relevant rights holders where permission is required, particularly for commercial use or redistribution of Monodepth2.
