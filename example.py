import models.config as config
import models.osim_parser as osim_parser

robot_pi = osim_parser.Osim2PinocchioModel()
robot_pi.parseModel(config.model_path,config.mesh_path)

robot_py = osim_parser.Osim2PythonModel()
PyModel = robot_py.readModel(config.model_path)
