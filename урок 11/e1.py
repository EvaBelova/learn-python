import sympy
from math import *
from sympy import lambdify, diff
from scipy.optimize import fsolve
from sympy.abc import x
from sympy.core.symbol import Symbol
func_np = lambdify(x, '-12*x**4*sin(cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30', modules=['numpy'])
solution = fsolve(func_np, 10)
print(solution)

dif_expr = diff('-12*x**4*sin(cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30', x)
print(dif_expr)

func_np = sympy.lambdify(x, dif_expr, modules=['numpy'])
solution = fsolve(func_np, 10)
print(solution)

x = Symbol('x')
f = '-12*x**4*sin(cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30'
sympy.plot(f)