# Write your code here :-)
import numpy as np

def f(x):
    return np.exp(x)

def df_exact(x):
    return np.exp(x)

x = 1.5
h_values = [10**(-i) for i in range(1, 16)]

print(f"{'h':>12} {'Numerisk df':>20} {'Eksakt df':>15} {'Feil':>15}")
print("-" * 65)

for h in h_values:
    df_numerisk = (f(x + h) - f(x - h)) / (2 * h)
    df_eksakt = df_exact(x)
    feil = abs(df_numerisk - df_eksakt)
    print(f"{h:12.1e} {df_numerisk:20.10f} {df_eksakt:15.10f} {feil:15.10f}")
