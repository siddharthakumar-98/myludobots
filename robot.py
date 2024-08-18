import pybullet as p
import pyrosim.pyrosim as pyrosim

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
	def __init__(self):
		self.motors = {}
		self.robotId = p.loadURDF("body.urdf")
		self.sensors = {}
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()
		
	def Prepare_To_Sense(self):
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)
			
	def Sense(self, t):
		for sensor in self.sensors.values():
			sensor.Get_Value(t)
			
	def Prepare_To_Act(self):
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)
			
	def Act(self, t):
		for jointName, motor in self.motors.items():
			motor.Set_Value(t, self.robotId)
			
	def Save_Values(self):
		for sensor in self.sensors.values():
			sensor.Save_Values()

		for motor in self.motors.values():
			motor.Save_Values()