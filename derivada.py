# Para instalar a dependência, execute no terminal: pip install sympy
from sympy import cos, diff, symbols

# Calcula e exibe a derivada de cos(x) em relação a x.
x = symbols('x')
print(diff(cos(x), x))