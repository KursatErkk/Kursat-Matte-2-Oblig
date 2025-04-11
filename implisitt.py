# Write your code here :-)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

L = 1.0
T = 0.5
nx = 20
nt = 100
h = L / nx
k = T / nt
alpha = k / h**2

x = np.linspace(0, L, nx+1)
u = np.zeros((nt+1, nx+1))
u[0, :] = np.sin(np.pi * x)

main_diag = (1 + 2*alpha) * np.ones(nx-1)
off_diag = -alpha * np.ones(nx-2)
A = np.diag(main_diag) + np.diag(off_diag, 1) + np.diag(off_diag, -1)

for j in range(nt):
    u_next = np.linalg.solve(A, u[j, 1:-1])
    u[j+1, 1:-1] = u_next

# Animasjon
fig, ax = plt.subplots()
line, = ax.plot(x, u[0])

def update(frame):
    line.set_ydata(u[frame])
    ax.set_title(f"t = {frame * k:.3f}")
    return line,

ani = FuncAnimation(fig, update, frames=range(0, nt+1, 2), blit=True)
plt.show()
