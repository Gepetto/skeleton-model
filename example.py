import models.config as config
import models.osim_parser as osim_parser

robot_pi = osim_parser.Osim2PinocchioModel()
robot_pi.parseModel(config.model_path,config.mesh_path)

robot_py = osim_parser.Osim2PythonModel()
PyModel = robot_py.readModel(config.model_path)


# viewer 
robotName = "Robot"
robotNode = 'world/'+robotName+'/'
mesh_path='/galo/devel/gepetto/Models/data/whole_body/obj'
generic_model='/galo/devel/gepetto/Models/data/whole_body/wholebody.osim'
from hqp.wrapper import Wrapper
from hqp.viewer_utils import Viewer
robot = Wrapper(generic_model, mesh_path, robotName, True)
viewer=Viewer('viewer',robot)
viewer.initDisplay("world/pinocchio")
nodeName = "world/"+robotName
viewer.loadDisplayModel(nodeName, "pinocchio", robot)
viewer.display(robot.q0,robotName)
viewer.setVisibility("Robot/floor", "OFF")
