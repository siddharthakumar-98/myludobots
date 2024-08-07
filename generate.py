import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("box.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = height/2.0
mod = 1
for i in range(0,9):	
	pyrosim.Send_Cube(name="Box", pos=[x,y,z+i] , size=[length*mod,width*mod,height*mod])
	mod = mod * 0.9
pyrosim.End()