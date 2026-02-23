import numpy as np
import matplotlib.pyplot as plt

g = 9.8
v0 = 20
theta = np.radians(45)

t = np.linspace(0, 3, 100)

x = v0*np.cos(theta)*t
y = v0*np.sin(theta)*t - 0.5*g*t**2

plt.plot(x, y)
plt.xlabel("Distance")
plt.ylabel("Height")
plt.title("Projectile Motion")
plt.grid()
plt.savefig("projectile_motion.png")
plt.show()