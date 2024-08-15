import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import math
import random
import constants as c

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(c.num_steps)
frontLegSensorValues = np.zeros(c.num_steps)
targetBackLegAngles = np.zeros(c.num_steps)
targetFrontLegAngles = np.zeros(c.num_steps)

targetFrontLegAngles = c.amplitudeFrontLeg * np.sin(c.frequencyFrontLeg * np.linspace(0, 2 * math.pi, num=c.num_steps, endpoint=True) + c.phaseOffsetFrontLeg)
targetBackLegAngles = c.amplitudeBackLeg * np.sin(c.frequencyBackLeg * np.linspace(0, 2 * math.pi, num=c.num_steps, endpoint=True) + c.phaseOffsetBackLeg)
#np.save("data/targetAngles.npy",targetAngles)
np.save("data/targetFrontLegAngles.npy", targetFrontLegAngles)
np.save("data/targetBackLegAngles.npy", targetBackLegAngles)

for i in range(c.num_steps):
    p.stepSimulation()
    
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_BackLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetBackLegAngles[i],
        maxForce=250)
    
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_FrontLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetFrontLegAngles[i],
        maxForce=250)
    
    time.sleep(1/500.0)

print(backLegSensorValues)
np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
p.disconnect()
