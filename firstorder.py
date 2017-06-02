from math import * 
from sympy import *
import numpy as np 

def solver (a,b,c):
	print("This is a solution to the linear first order differential equation ay' + by = c where the answer is:")

	x= symbols('x')
		#Case 1:
	if c==0:
			print("The homogeneous solution is")
			p = (b/a) 
			P = -1.0 * integrate(p,x)
			P = str(P)
			return([P])
 		#Case 2:
	elif c!=0:
			print("The combination of the homogeneous solution and the particular solution")
			p = (b/a) 
			P = -1.0 * integrate(p,x)
			N = (c/b)
			N = str(N)	
			P = str(P)
			return([P,N])
		#Case 3:
	# else c==

def main ():
	x= symbols('x')
	a=1.0
	b=2.0
	c=18.0
	k= solver(a,b,c)
	if c==0:
		Solution= "A*exp["+k[0]+"]"
	elif c!=0:
		Solution= "A*exp["+k[0]+"]+(" +k[1]+ ")."
	print(Solution)
main()