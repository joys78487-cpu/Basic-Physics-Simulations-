import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def model(y, t):
    x, v = y
    k = 4
    m = 1
    dxdt = v
    dvdt = -k/m * x
    return [dxdt, dvdt]

y0 = [1, 0]
t = np.linspace(0, 10, 100)

sol = odeint(model, y0, t)

plt.plot(t, sol[:,0])
plt.xlabel("Time")
plt.ylabel("Displacement")
plt.title("Spring Mass Oscillation")
plt.grid()
plt.savefig("spring_mass.png")
plt.show()