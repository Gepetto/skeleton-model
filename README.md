# Models
Some biomechanical and robotic models 
##Characteristics:
  - Allows to parse .osim OpenSim models to pinocchio and/or python models
  
##Setup
```json
   $ python setup.py --prefix='your install path'
```

##Required Dependencies:
- Python 2.7, Numpy

##Extra Dependencies:
If you want to build a pinocchio model
- Pinocchio: librari for rigid multi-body dynamics. Can be download from here: http://stack-of-tasks.github.io/pinocchio/
If you want to visualize your pinocchio model:
- Gepetto-viewer: A graphical interface for pinocchio. Can be downloaded from here:
    https://github.com/humanoid-path-planner/gepetto-viewer.git
- Gepetto-viewer-corba: CORBA server/client for the Graphical Interface of Pinocchio. Can be downloaded from here:
    https://github.com/humanoid-path-planner/gepetto-viewer-corba.git

##Biomechanical Models (.osim):
 - Whole-body model: 23 segments, 42 DoF including spherical joints, 30 muscles, 48 virtual markers. Based on existing models of OpenSim and Dumas et al 2006.
 
  ![Alt text](/relative/path/to/img.jpg?raw=true "Whole-body model")

