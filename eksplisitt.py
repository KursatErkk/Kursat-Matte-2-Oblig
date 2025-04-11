# Write your code here :-)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

L = 1.0
T = 0.1
nx = 20
nt = 100
h = L / nx
k = T / nt
alpha = k / h**2

x = np.linspace(0, L, nx+1)
t = np.linspace(0, T, nt+1)

u = np.zeros((nt+1, nx+1))
u[0, :] = np.sin(np.pi * x)

for j in range(nt):
    for i in range(1, nx):
        u[j+1, i] = u[j, i] + alpha * (u[j, i+1] - 2*u[j, i] + u[j, i-1])

fig, ax = plt.subplots()
line, = ax.plot(x, u[0])
ax.set_ylim(0, 1)
ax.set_title("Eksplisitt skjema – løsning over tid")
ax.set_xlabel("x")
ax.set_ylabel("u(x,t)")

def update(frame):
    line.set_ydata(u[frame])
    ax.set_title(f"t = {t[frame]:.4f}")
    return line,

ani = FuncAnimation(fig, update, frames=nt+1, interval=100)
plt.show()
