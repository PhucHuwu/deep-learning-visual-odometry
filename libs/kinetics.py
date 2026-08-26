import torch


def rot_from_euler_angle(angle):
    """Convert euler angles to rotation matrix.
     Reference: https://github.com/pulkitag/pycaffe-utils/blob/master/rot_utils.py#L174
    Args:
        angle: rotation angle along 3 axis (in radians) -- size = [B, 3]
    Returns:
        Rotation matrix corresponding to the euler angles -- size = [B, 3, 3]
    """
    B = angle.size(0)
    x, y, z = angle[:, 0], angle[:, 1], angle[:, 2]

    cosz = torch.cos(z)
    sinz = torch.sin(z)

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

    None
    None
    None

    pass


def from_euler_t(euler_angle, translation, invert=False):
    None
    None

    if invert:
        None

    pass
