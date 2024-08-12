import matplotlib.pyplot as plt
import numpy as np

'''
bl_data = np.load("data/backLegSensorValues.npy")
fl_data =  np.load("data/frontLegSensorValues.npy")
plt.plot(bl_data, label="backleg", linewidth=1)
plt.plot(fl_data, label="frontleg")
'''
tang = np.load("data/targetAngles.npy")
plt.plot(tang)
plt.legend()
plt.show()