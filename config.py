import pinocchio as se3
oMp = se3.utils.rotate('z',np.pi/2) * se3.utils.rotate('x',np.pi/2)
mesh_path = 'whole_body/stl_osim'
model_path = 'whole_body/wholebody.osim'
