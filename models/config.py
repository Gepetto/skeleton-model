import pinocchio as se3
import numpy as np
import os
oMp = se3.utils.rotate('z',np.pi/2) * se3.utils.rotate('x',np.pi/2)
