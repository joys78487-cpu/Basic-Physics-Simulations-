import numpy as np
import matplotlib.pyplot as plt

g = 9.8
y0 = 100
v0 = 0

t = np.linspace(0, 5, 100)
y = y0 + v0*t - 0.5*g*t**2

plt.plot(t, y)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Free Fall Simulation")
plt.grid()
plt.savefig("free_fall.png")
plt.show()