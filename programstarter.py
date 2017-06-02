from math import *
from sympy import *
import numpy as np

a,b,c,x = symbols('a,b,c,x')

#f = a*x**2 + b*x + c
#f = a*x**4
f = 3.0 / ((2.0*x)+2)
#f = Function('f')
x = Symbol('x')
#fprime = f(x).diff(x) - f(x) # f' = f(x)
F = integrate(f,x)
F = str(F)
# y = dsolve(fprime, f(x))
y = Symbol('y')
eqn = Eq(((3.0)/(2.0)*(np.log(2*y+2)), 1)
# print y
print(f)
#print y.subs(x,4)
#print [y.subs(x, X) for X in [0, 0.5, 1]] # multiple values
#solution = solve(f, x)
#print solution
#print(F) 
#print integrate(f, x)          # indefinite integral
#print integrate(f, (x, 0, 1))  # definite integral from x=0..1
#print diff(f, x)
#print diff(f, x, 2)	# 2nd part differentiate respect to x, 3rd part; the number represents amount of derivatives taken
#print diff(f, a)

############Program for computing the height of a ball in vertical motion###############################

	#v_0 = 5 #initial velocity
	#g = 9.81 #acceleration of gravity
	#t = 0.6 #time
	#y = v_0*t - 0.5*g*t**2 #vertical position
	#print(y)

###################Program for conversion from Celcius to Fahrenheit##########################
#C = 21
#F = (9/5)*C +32
#print(F)