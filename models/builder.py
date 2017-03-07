import pinocchio as se3
import numpy as np
class Pinocchio:
   def __init__(self):
      # Pinocchio Model
      self.model = se3.Model.BuildEmptyModel()
      self.data = []
      # Skelette Meshes
      self.visuals = []
      self.visuals.append([0,'ground','none'])
      self.forces = []
      self.FrameType = se3.FrameType.OP_FRAME
             
   def buildModel(self, parent, joint_model, joint_placement, joint_name,
                            joint_id, body_inertia, body_placement, body_name):
      ''' Add a model to the kinematic three
      TODO add with bounds, check model.hpp
      '''
      self.model.addJoint(parent, joint_model, joint_placement, joint_name)
      self.model.addJointFrame(joint_id, joint_id)
      ''' Append a body to the given joint in the kinematic tree
      '''
      self.model.appendBodyToJoint(joint_id, body_inertia, body_placement)
      self.model.addBodyFrame(body_name, joint_id, body_placement, parent)
      ''' Add a frame to the frame three i.e. operational points
      '''
      #self.model.addFrame(joint_name, parent, idx_f, body_placement, self.FrameType)
      return self.model
      
   def createVisuals(self, parent, joint_name, filename, scale_factors=None, transform=None):
      self.visuals.append([parent, joint_name, filename, scale_factors, transform ])
      return self.visuals

   def createForces(self,force_name,force_type,parent,points):
      self.forces.append([force_name,force_type,parent,points])
      return self.forces

   def addJointConstraints(self, qRoM):
      self.lowerPositionLimit = np.matrix(qRoM)[:,0]
      self.upperPositionLimit = np.matrix(qRoM)[:,1]
      return self.lowerPositionLimit,self.upperPositionLimit
   
   def createData(self):
      self.data = self.model.createData()
      return self.data
   
