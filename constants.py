import math
import numpy as np

num_steps = 2000

x = np.linspace(0, 2*np.pi, num=num_steps)

amplitude = math.pi/4
frequency = 10
offset = 0

amplitudeFrontLeg = math.pi / 4
frequencyFrontLeg = 10
phaseOffsetFrontLeg = 0

amplitudeBackLeg = math.pi / 4
frequencyBackLeg = 10
phaseOffsetBackLeg = math.pi / 4

targetMin = -math.pi / 4.0
targetMax = math.pi / 4.0

maxForce = 250

timeSleep = 1/100.0