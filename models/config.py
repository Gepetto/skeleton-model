import pinocchio as se3
import numpy as np
import os
oMp = se3.utils.rotate('z',np.pi/2) * se3.utils.rotate('x',np.pi/2)
actual_path = os.path.dirname(os.path.abspath('HQP'))
mesh_path = actual_path+'/Models/whole_body/stl_osim'
model_path = actual_path+'/Models/whole_body/wholebody.osim'
