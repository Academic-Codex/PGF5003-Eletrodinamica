import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Potencial de carga pontual em (0,0)
V = 1/np.sqrt(X**2 + Y**2)

plt.figure(figsize=(6,5))
plt.contourf(X, Y, V, levels=50, cmap='coolwarm')
plt.colorbar(label='Potencial (V)')
plt.title('Potencial Elétrico - Carga Pontual')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('potencial_pontual.pdf', bbox_inches='tight')

# Campo elétrico
Ex = X/(X**2 + Y**2)**(3/2)
Ey = Y/(X**2 + Y**2)**(3/2)

plt.figure(figsize=(6,5))
plt.streamplot(X, Y, Ex, Ey, color='k', density=1.5)
plt.title('Campo Elétrico - Carga Pontual')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('campo_pontual.pdf', bbox_inches='tight')

