import pinocchio as se3
import numpy as np
import os
oMp = se3.utils.rotate('z',np.pi/2) * se3.utils.rotate('x',np.pi/2)
model_path = 'data/whole_body/wholebody.osim'
mesh_path = 'data/whole_body/obj/'
