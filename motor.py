import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c

class MOTOR:
	def __init__(self, jointName):
		self.jointName = jointName
		self.motorValues = np.zeros(c.num_steps)
		self.Prepare_To_Act()

	def Prepare_To_Act(self):
		self.amplitude = c.amplitude
		self.frequency = c.frequency
		self.offset = c.offset
		
		self.targetMin = c.targetMin
		self.targetMax = c.targetMax

		if self.jointName == 'Torso_BackLeg':
			self.frequency /= 2.0
		
		self.motorValues = self.amplitude * np.sin(self.frequency * np.linspace(self.targetMin, self.targetMax, num=c.num_steps, endpoint=True) + self.offset)

	def Set_Value(self, desiredAngle, robotId):
		pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,
                            jointName = self.jointName,
                            controlMode = p.POSITION_CONTROL,
                            targetPosition = desiredAngle,
                            maxForce = c.maxForce)

	def Save_Values(self):
		np.save('data/{self.jointName}_MotorValues.npy', self.motorValues)