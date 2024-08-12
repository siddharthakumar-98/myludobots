import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import math
import time
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(500)
frontLegSensorValues = np.zeros(500)

targetMin = -math.pi / 2.0
targetMax = math.pi / 2.0

num_steps = 500
x = np.linspace(0, 2 * math.pi, num_steps)
targetAngles = (targetMax - targetMin) / 2.0 * np.sin(x) + (targetMax + targetMin) / 2.0

for i in range(0,500):
	p.stepSimulation()
	
	targetBackLeg = targetAngles[i]
	targetFrontLeg = targetAngles[i]
	
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	
	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
	jointName = b'Torso_BackLeg',
	controlMode = p.POSITION_CONTROL,
	targetPosition = targetBackLeg,
	maxForce = 250)
	
	
	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
	jointName = b'Torso_FrontLeg',
	controlMode = p.POSITION_CONTROL,
	targetPosition = targetFrontLeg,
	maxForce = 250)
	
	time.sleep(1/60.0)
print(backLegSensorValues)
np.save("data/backLegSensorValues.npy",backLegSensorValues)
np.save("data/frontLegSensorValues.npy",frontLegSensorValues)
p.disconnect()