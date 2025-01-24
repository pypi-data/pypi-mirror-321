import os
import numpy as np

DATA = np.load(os.path.join(
    os.path.dirname(__file__), 'x256.npz'
))
RGB_X256 = DATA['arr_0']
X256_RGB = DATA['arr_1']


def from_rgb(
    r: np.ndarray, g: np.ndarray, b: np.ndarray,
    weighted: bool = False,
    n_color: int = 232
) -> np.ndarray:
    _e = (
        2 if n_color == 256 else 0
    ) + (
        1 if weighted else 0
    )
    return RGB_X256[_e, r, g, b]


def to_rgb(x: np.ndarray) -> np.ndarray:
    return X256_RGB[x]
