import pybullet as p

class WORLD:

    def __init__(self):

        self.planeId = p.loadURDF("plane.urdf")
        self.boxId = p.loadURDF("cube.urdf")
        p.loadSDF("world.sdf")