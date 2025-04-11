import numpy as np
import matplotlib.pyplot as plt

L = 1.0
T = 0.1
nx = 20
nt = 100
h = L / nx
k = T / nt
alpha = k / h**2
x = np.linspace(0, L, nx+1)
t = np.linspace(0, T, nt+1)

def u_exact(x, t):
    return np.sin(np.pi * x) * np.exp(-np.pi**2 * t)


def make_matrix(method):
    N = nx - 1
    if method == "implicit":
        a = -alpha * np.ones(N - 1)
        b = (1 + 2*alpha) * np.ones(N)
        c = -alpha * np.ones(N - 1)
    elif method == "cn":
        a = -alpha/2 * np.ones(N - 1)
        b = (1 + alpha) * np.ones(N)
        c = -alpha/2 * np.ones(N - 1)
    A = np.diag(b) + np.diag(a, 1) + np.diag(c, -1)
    return A


def crank_nicolson():
    u = np.zeros((nt+1, nx+1))
    u[0, :] = np.sin(np.pi * x)

    A = make_matrix("cn")
    B = make_matrix("cn")
    B = 2*np.eye(nx-1) - A  

    for j in range(nt):
        rhs = B @ u[j,1:-1]
        u[j+1,1:-1] = np.linalg.solve(A, rhs)
    return u

def implicit():
    u = np.zeros((nt+1, nx+1))
    u[0, :] = np.sin(np.pi * x)
    A = make_matrix("implicit")

    for j in range(nt):
        rhs = u[j,1:-1]
        u[j+1,1:-1] = np.linalg.solve(A, rhs)
    return u

def explicit():
    u = np.zeros((nt+1, nx+1))
    u[0, :] = np.sin(np.pi * x)

    for j in range(nt):
        for i in range(1, nx):
            u[j+1, i] = u[j, i] + alpha*(u[j, i+1] - 2*u[j, i] + u[j, i-1])
    return u

u_expl = explicit()
u_impl = implicit()
u_cn   = crank_nicolson()
u_ana  = u_exact(x, T)

plt.figure(figsize=(10, 6))
plt.plot(x, u_expl[-1], '--', label='Eksplisitt')
plt.plot(x, u_impl[-1], '-.', label='Implisitt')
plt.plot(x, u_cn[-1], '-', label='Crank-Nicolson')
plt.plot(x, u_ana, 'k:', label='Analytisk')
plt.title(f"Sammenlikning av metoder ved t = {T}")
plt.xlabel("x")
plt.ylabel("u(x,T)")
plt.legend()
plt.grid(True)
plt.show()