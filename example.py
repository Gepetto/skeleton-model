import config
import osim_parser

robot = osim_parser.Osim2PinocchioModel()
robot.parseModel(config.model_path)
