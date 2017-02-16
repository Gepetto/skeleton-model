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

Model
GX3
Whole body model that consists of 23 bodies, 42 degrees of freedom
, 
30 muscles
and 
48 virtual markers
. 
The geometric  model together with the  lower limbs,  pelvis  and  upper  limbs anthropometry are based on the running model of Hammer et al. 2010. The mentioned model consists of 12 segments and 29 degrees of freedom. 
Extra segments and degrees of freedom were added based on Dumas et al. 2007. 

Each lower extremity has seven degrees of freedom; the hip was modeled as a ball-and-socket joint, the knee is modeled as a revolute joint, the ankle is modeled as 2 revolute  joints (flexion-extension  and inversion-eversion) and the toes with one revolute joint at the metatarsals.

The pelvis joint is modeled as a free flyer joint to allow the model to translate and rotate in the 3D space, the lumbar motion is modeled as a ball-and-socket joint (Anderson and Pandy, 1999) and the neck joint is also modeled as a ball-and-socket joint. Mass properties of the torso and head (including the neck) segments are estimated fromDumas et al., 2007. 

Each arm consist of 8 degrees-of-freedom; the shoulder is modeled as a ball-and-socket joint,the elbow and forearmrotation are modeled with revolute joints to represent flexion-extension and pronation-supination (Holzbaur et al., 2005), the wrist flexion-extension and radial-ulnar deviation  are modeled  with  revolute  joints, and the hand fingers are modeled with one revolute joint for all fingers. Mass properties for the arms were estimated from Anderson et al. 1999, and de Leva, 1996. 

The  model  also  includes  a  whole-body  marker  set  with  48  markers  placed  in anatomical landmarks selected as suggested in Wu et al. 2002, 2005. 

Lastly, the model contains 30 superficial muscles that represent the more important stabilizer muscles of the  whole-body. The  muscle-set  was chosen in order to  study  highly  dynamic motion. 

The neutral position of the model is the anatomical pose and a half-sitting position was also added.

The geometrical models of the bones (meshes) are provided as *.vtp (compatible with OpenSim) and *.stl
(compatible with OpenSim, Gepetto Viewer and Blender).
 
  ![Alt text](https://github.com/GaloMALDONADO/Models/blob/master/images/whole_body.png?raw=true "Whole-body model")

