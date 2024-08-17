import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import pybullet as p
import time
from world import WORLD
from robot import ROBOT

class SIMULATION:

	def __init__(self):
		
		self.physicsClient = p.connect(p.GUI)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
		p.setGravity(0, 0, -9.8)
		
		self.world = WORLD()
		self.robot = ROBOT()
		
		pyrosim.Prepare_To_Simulate(self.robot.robotId)
