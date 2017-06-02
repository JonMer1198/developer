from scipy import (
	symbols,	#define mathematical symbols for symbolic mathematical
	diff,	#differentiate expressions
	integrate,	#integrate expressions
	Rational,	#define rational numbers
	lambdify,	#turn symbolic expressions into Python functions
	)
t, v0, g = symbols('t v0 g')
y= v0*t -Rational(1,2)*g*t**2
dydt= diff(y, t)
dydt-g*t + v0
print 'acceleration:', diff(y, t, t)	#2nd derivative acceleration: -g
y2= integrate(dydt, t)
y2 -g*t**2/2 +t*vo