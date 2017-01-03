import xml.etree.ElementTree as xml
import numpy as np
import pinocchio as se3
import os 
from builder import Pinocchio as pm
import config


''' **************** OPENSIM 2 PYTHON MODEL **************** '''

class Osim2PythonModel:
    def __init__(self):
        #self.PyModel = {'Bodies':[], 'Joints':[], 'Visuals':[]}
        #self.default_joint = 
        Y = [[ 0.001,   0.    ,   0. ],
             [ 0.,       0.0001,   0. ],
             [ 0.,       0.,       0.0001]]
        self.default_body = {'name':['body'], 
                             'mass': ['0.1'], 
                             'mass_center': [['0', '0', '0']], 
                             'inertia':[Y]}
        self.default_visual = []
        visual_data = {'scale_factors':[['1','1','1']],
                       'show_axes':[['false']],
                       'display_preference':['4']}
        bone_data = {'color': [['1', '1', '1']],
                     'display_preference': ['4'],
                     'geometry_file' : ['None'],
                     'opacity':['1'],
                     'scale_factors':[['1','1','1','1']],
                     'transform':[['0','0','0','0','0','0']] }
        self.default_visual.append([visual_data, bone_data])
        
        self.default_joint = []
        joint_data = {'name':['joint'],
                      'parent_body':[],
                      'location_in_parent':[['0','0','0']],
                      'orientation_in_parent':[['0','0','0']],
                      'location':[['0','0','0']],
                      'orientation':[['0','0','0']]}
        coordinate_data = {'name':['dof'],
                           'motion_type':[],
                           'default_value':[],
                           'default_speed_value':[['0','0','0']],
                           'range':[['0','0']],
                           'clamped':['false'],
                           'locked':['false'],
                           'prescribed_function':[None]}
        spatial_data = {'name': [['rotation1'],
                                 ['rotation2'],
                                 ['rotation3'],
                                 ['translation1'],
                                 ['translation2'],
                                 ['translation3']],
                        'coordinates': [],
                        'axis': [['1','0','0'],
                                ['0','1','0'],
                                ['0','0','1'],
                                ['1','0','0'],
                                ['0','1','0'],
                                ['0','0','1']]}
        self.default_joint.append([joint_data, coordinate_data, spatial_data])

    def readModel(self,filename):
        PyModel = {'Bodies':[], 'Joints':[], 'Visuals':[]}
        tree = xml.parse(filename)
        root = tree.getroot()
        # get body set
        for bodies in root.findall('./Model/BodySet/objects/Body'):
            body_data = {'name':[], 
                         'mass':[], 
                         'mass_center':[], 
                         'inertia':[]}
            body_data['name'].append(bodies.get('name'))
            body_data['mass'].append(bodies.find('mass').text)
            body_data['mass_center'].append((bodies.find('mass_center').text).split())
            Y = [[bodies.find('inertia_xx').text,
                  bodies.find('inertia_xy').text,
                  bodies.find('inertia_xz').text],
                 [bodies.find('inertia_xy').text,
                  bodies.find('inertia_yy').text,
                  bodies.find('inertia_yz').text],
                 [bodies.find('inertia_xz').text,
                  bodies.find('inertia_yz').text,
                  bodies.find('inertia_zz').text]]
            body_data['inertia'].append(Y)
            PyModel['Bodies'].append(body_data)

            # Joints
            joints_list =  bodies.iter('CustomJoint')
            for joint in joints_list:
                joint_data = {'name':[], 
                              'parent_body':[], 
                              'location_in_parent':[], 
                              'orientation_in_parent':[], 
                              'location':[],
                              'orientation':[]}
                joint_data['name'].append(joint.get('name'))
                joint_data['parent_body'].append(joint.find('parent_body').text)
                joint_data['location_in_parent'].append((joint.find('location_in_parent').text).split())
                joint_data['orientation_in_parent'].append((joint.find('orientation_in_parent').text).split())
                joint_data['location'].append((joint.find('location').text).split())
                joint_data['orientation'].append((joint.find('orientation').text).split())

                # Coordinate Set
                coordinates_list = joint.iter('Coordinate')
                coordinate_data = {'name':[],
                                   'motion_type':[],
                                   'default_value':[],
                                   'default_speed_value':[],
                                   'range':[],
                                   'clamped':[],
                                   'locked':[],
                                   'prescribed_function':[],
                                   }
                for coordinates in coordinates_list:
                    coordinate_data['name'].append(coordinates.get('name'))
                    coordinate_data['motion_type'].append(coordinates.find('motion_type').text)
                    coordinate_data['default_value'].append(coordinates.find('default_value').text)
                    coordinate_data['default_speed_value'].append(coordinates.find('default_speed_value').text)
                    coordinate_data['range'].append((coordinates.find('range').text).split())
                    coordinate_data['clamped'].append(coordinates.find('clamped').text)
                    coordinate_data['locked'].append(coordinates.find('locked').text)
                    coordinate_data['prescribed_function'].append(coordinates.find('prescribed_function').text)
                               
                #get spatial transform
                spatial_list = joint.iter('TransformAxis')
                spatial_data = {'name': [],
                                'coordinates': [],
                                'axis': []}
                for spatial_transform in spatial_list:
                    spatial_data['name'].append(spatial_transform.get('name'))
                    spatial_data['coordinates'].append(spatial_transform.find('coordinates').text)
                    spatial_data['axis'].append((spatial_transform.find('axis').text).split())

                PyModel['Joints'].append([joint_data, coordinate_data, spatial_data])

            # Visible Objects
            visible_list =  bodies.iter('VisibleObject')
            for visuals in visible_list:
                visuals_data = {'scale_factors':[],
                                'show_axes':[],
                                'display_preference':[]}
                visuals_data['scale_factors'].append((visuals.find('scale_factors').text).split())
                visuals_data['show_axes'].append(visuals.find('show_axes').text)
                visuals_data['display_preference'].append(visuals.find('display_preference').text)
                
                bones_list =  visuals.iter('DisplayGeometry')
                bones_data = {'geometry_file': [],
                                'color': [],
                                'transform': [],
                                'scale_factors': [],
                                'display_preference': [],
                                'opacity': []}
                for bones in bones_list:
                    bones_data['geometry_file'].append(bones.find('geometry_file').text) 
                    bones_data['color'].append((bones.find('color').text).split())
                    bones_data['transform'].append((bones.find('transform').text).split())
                    bones_data['scale_factors'].append((bones.find('scale_factors').text).split())
                    bones_data['display_preference'].append(bones.find('display_preference').text)
                    bones_data['opacity'].append(bones.find('opacity').text)
                
                PyModel['Visuals'].append([visuals_data, bones_data])
        return PyModel        









''' **************** OPENSIM 2 PINOCCHIO MODEL **************** '''
class Osim2PinocchioModel:
    def __init__(self):
        self.builder = pm()
        self.model = self.builder.model
        self.joint_models = []
        self.visuals = self.builder.visuals
        self.joint_limits = self.builder.joint_limits
        self.data = self.builder.data

    def __OpenSimJointsToPynocchioJoints(self, PyModel):
        jts = 0 
        for joints in PyModel['Joints']:
            
            dof_in_joint = 6 - (joints[2]['coordinates']).count(None)
            if dof_in_joint == 6:
                self.joint_models.append([jts, PyModel['Joints'][jts][0]['name'][0], se3.JointModelFreeFlyer()])
            elif dof_in_joint == 3:
                self.joint_models.append([jts,PyModel['Joints'][jts][0]['name'][0], se3.JointModelSpherical()])
            elif dof_in_joint == 2:
                print '2 dof not supported'
            elif dof_in_joint == 1:
                for dof in range(0, len(joints[2]['coordinates'])):
                    if joints[2]['coordinates'][dof] != None:
                        if joints[2]['name'][dof][0:8] == 'rotation':
                            if joints[2]['axis'][dof] == ['1', '0', '0']:
                                self.joint_models.append([jts,PyModel['Joints'][jts][0]['name'][0],se3.JointModelRY()])#Y
                            elif joints[2]['axis'][dof] == ['0', '1', '0']:
                                self.joint_models.append([jts,PyModel['Joints'][jts][0]['name'][0],se3.JointModelRZ()])#Z
                            elif joints[2]['axis'][dof] == ['0', '0', '1']:
                                self.joint_models.append([jts,PyModel['Joints'][jts][0]['name'][0],se3.JointModelRX()])#X
                            else:
                                v=np.matrix( [np.float64(joints[2]['axis'][dof][0]),
                                              np.float64(joints[2]['axis'][dof][1]), 
                                              np.float64(joints[2]['axis'][dof][2])] )
                                self.joint_models.append([jts,PyModel['Joints'][jts][0]['name'][0],
                                                     se3.JointModelRevoluteUnaligned(v[0,2], v[0,0], v[0,1])])#2,0,1
            jts += 1                    
        return self.joint_models
        
    
    def buildModel(self, PyModel=None, filename=None, mesh_path=None):
        ''' \ brief build a Pinocchio model given a PyModel
        \param[in] PyModel The python model which can be created using readOsim. Default is None
        \param[in] filename Path and name of the *.osim file which is used in case PyModel is not provided
        \param[out] model Pinocchio model
        '''
        if PyModel is None:
            # read osim model and store in python model
            py=Osim2PythonModel()
            PyModel = py.readModel(filename)
        
        osMpi = se3.utils.rotate('z', np.pi/2) * se3.utils.rotate('x', np.pi/2)
        joint_models = self.__OpenSimJointsToPynocchioJoints(PyModel)
        
        
        id = []
        for joint in range(0,len(PyModel['Joints'])):
            parent_name = PyModel['Joints'][joint][0]['parent_body'][0]
            id.append(parent_name)
        
        
        for joint in range(0,len(PyModel['Joints'])):
            # don't take into account ground body and visual
            body = joint  + 1
            body_name = PyModel['Bodies'][body]['name'][0]
            joint_name = PyModel['Joints'][joint][0]['name'][0] 
            joint_id = body
            parent = id.index(PyModel['Joints'][joint][0]['parent_body'][0])
            joint_model = joint_models[joint][2]

            print 'ID: ',joint_id
            print 'Joint Name: '+joint_name
            print 'Parent Name :'+PyModel['Joints'][joint][0]['parent_body'][0], parent
            print 'Joint Model: ',joint_model
            
            
            ''' From OpenSim to Pinocchio
            '''
            joint_placement = se3.SE3.Identity()
            r = np.matrix(PyModel['Joints'][joint][0]['orientation_in_parent'][0],dtype = np.float64).T
            joint_placement.rotation = se3.utils.rpyToMatrix(osMpi * r)
            
            t = PyModel['Joints'][joint][0]['location_in_parent'][0]            
            joint_placement.translation = osMpi *  np.matrix(t,dtype=np.float64).T
            
            mass = np.float64(PyModel['Bodies'][body]['mass'][0])
            mass_center = osMpi * np.matrix(PyModel['Bodies'][body]['mass_center'][0], dtype = np.float64).T
            inertia_matrix = np.matrix(PyModel['Bodies'][body]['inertia'][0], dtype = np.float64)
            body_inertia = (se3.Inertia( mass, mass_center, inertia_matrix))
            body_placement = se3.SE3.Identity()
            
            # Add to pynocchio model
            self.model = self.builder.buildModel(parent, joint_model,joint_placement,
                                                 joint_name,joint_id, body_inertia,
                                                 body_placement, body_name)
            self.data = self.builder.createData()
            scale_factors = osMpi * (np.matrix(PyModel['Visuals'][body][0]['scale_factors'][0], np.float64)).T
            scale_factors = np.asarray(scale_factors.T)[0]
            scale_factors = [scale_factors[0], scale_factors[1], scale_factors[2]]

            # add to visuals list
            for mesh in range(0, len(PyModel['Visuals'][body][1]['geometry_file']) ):
                visual_name = os.path.splitext(PyModel['Visuals'][body][1]['geometry_file'][mesh])[0]
                filename = mesh_path+'/'+visual_name+'.stl'
                print 'Filename: '+filename
                transform = np.matrix(PyModel['Visuals'][body][1]['transform'][mesh],dtype=np.float64).T
                transform[3:6] =  osMpi  *transform[3:6]
                transform[0:3] =  osMpi * transform[0:3]
                self.visuals = self.builder.createVisuals(parent, joint_name, filename, scale_factors, transform)
           
            print '****'
        
    def parseModel(self, filename, mesh_path):
        ''' parseModel(filename)
        Parses an OpenSim Model to a Pinocchio Model
        '''
        py=Osim2PythonModel()
        return self.buildModel(py.readModel(filename), filename, mesh_path)


    






''' *************** UTILS ******************* '''
def readOsim(self, filename):
    '''
    get an osim filename .mot or .sto  and return data as a python dictionary which consist of
    time, data, col_headers, units
    '''
    Data = {'time': [], 'data': [], 'col_headers': [], 'units': []}
    file_extension = os.path.splitext(filename)[1][1:]
    print 'File extension is .'+file_extension
    if file_extension not in ['mot', 'sto']:
        print('File extension is not recognized. Method readIK reads only OpenSim .mot and .sto files')
        return
        
    try:
        f = open(filename, 'r')
    except IOError:
        print('cannot open', filename)
        
    with open(filename, 'r') as f:
        line = f.readline().split()[0]
        Data['filename'] = line
        print 'Reading file: '+line
            
        # Read Header
        while True:
            try:
                line = f.readline().split()[0]
            except IndexjError:
                line = f.readline()
                    
            if line[0:13] == 'inDegrees=yes':
                Data['units'] = 'degrees'
                print 'Angles are in degrees'
            elif line[0:9] == 'endheader':
                break        
        # Read Data
        Data['col_headers'] = f.readline().split()[1:]
        for rows in f:
            Data['data'].append(rows.split()[1:])
            Data['time'].append(float(rows.split()[0]))
        
    for rows in range (0,len(Data['data'][:])):
        for cols in range (0,len(Data['data'][0])):
            if cols in (3,4,5):
                # translations
                Data['data'][rows][cols] = float(Data['data'][rows][cols])
            else:
                Data['data'][rows][cols] = np.deg2rad(float(Data['data'][rows][cols]))
                #print np.deg2rad(float(data['values'][rows][cols]))
                               
    return Data 
