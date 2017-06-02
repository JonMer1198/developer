from math import * 

def solver (a,b,c):
	print("This is a solution to the second order homogenous differential equation ay'' + by' + cy = 0 where the answer has:")
	
		#Case 1:
	if b**2 - (4.0*a*c)==0:
			print("repeated roots")
			r1= (-b/(2.0*a))
			r2= (-b/(2.0*a))
			r1=str(r1)
			r2=str(r2)
			return([r1,r2])

		#Case 2:
	elif b**2 - (4.0*a*c)< 0:
			print("imaginary roots")
			re= (-b/(2.0*a))
			im= (((4.0*a*c)-b**2)**0.5)/(2.0*a)
			r1= re
			r2= im
			r1=str(r1)
			r2=str(r2)
			return([r1,r2])

		#Case 3:
	else:
			print("real roots")
			r1= (-b/(2.0*a)) +  ((b**2 - (4.0*a*c))**0.5)/(2.0*a)
			r2= (-b/(2.0*a)) -  ((b**2 - (4.0*a*c))**0.5)/(2.0*a)
			
			r1=str(r1) 
			r2=str(r2)
			return([r1,r2])

def main ():
	a=1
	b=(-4)
	c=5
	r=solver(a,b,c)
	if b**2 - (4.0*a*c) ==0:
		GeneralSolution= ("A*exp("+r[0]+"x) + Bx*exp("+r[1]+"x)")
	elif b**2 - (4.0*a*c)< 0:
		GeneralSolution= ("A*exp(("+r[0]+ "-" "" "i"+r[1]+")x) + B*exp(("+r[0]+ "+" "" "i"+r[1]+")x)")
	else:
		GeneralSolution= ("A*exp("+r[0]+"x) + B*exp("+r[1]+"x)")

	print(GeneralSolution)
main()
