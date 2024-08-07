import pybullet as p
import time
physicsClient = p.connect(p.GUI)
<<<<<<< HEAD
=======
p.loadSDF("box.sdf")
>>>>>>> onelink
for i in range(0,1000):
	p.stepSimulation()
	print(i)
	time.sleep(1/60.0)
p.disconnect()