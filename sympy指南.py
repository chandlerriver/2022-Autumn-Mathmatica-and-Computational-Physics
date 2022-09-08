import sympy

#Handbook of Symbolic Python


#define variables
x = sympy.Symbol("x")
y = sympy.Symbol("y")
z = sympy.Symbol("z")
#define variables end

#define functions
f = x**2 + x**4 + x**2 + 2*x**4
g = x**3 + x * y**2 + x*y*z
h = x**2 + sympy.cos(y**2) + z**x
I = x*(x**2+x*y+x*y**2)
J = sympy.sin(x) + sympy.cos(y)
#define functions end



#do it later
d = sympy.Derivative(h,x)
print(d)
print(d.doit())
#do it later end 

                            #polynomial arithmetic

#factoring
print("factor",end = " ")
print(sympy.factor(f))

#simplify
print("simplify",end= " ")
print(sympy.simplify(g))

#expand
print("expand",end = " ")
print(sympy.expand(I))

#collect
print("collect",end=" ")
print(sympy.collect(f,[x**2,x**4]))

#rewrite
print("rewrite",end = " ")
print(J.rewrite(sympy.tan(x)))

#series
print("series",end = " ")
print(J.series(x,0,10))

#solve
print("solve",end = " ")
print(x**2+x<10,x)

                            #calculus
#limit
print("limit",end = " ")
print(sympy.limit(sympy.sin(x)/x,x,0))

#calculate derivative and partial derivative
print(sympy.diff(g,z))
print(sympy.diff(f,x,3))

#integrate
print("sympy.integrate(f,x)",end = " ")
print(sympy.integrate(f,x))
print("sympy.integrate(f,(x,0,5))",end = " ")
print(sympy.integrate(f,(x,0,5)))

#dsolve
from sympy import Function,dsolve,Derivative,symbols,Eq
from sympy.abc import t
x = Function("x")
result = dsolve(Derivative(x(t),t,4)-22*Derivative(x(t),t,2)-24*x(t))
print("result",end="  ")
print(result)
print("ODEs")

x = Function("x")
y = Function("y")
eq=(Eq(Derivative(x(t),t,2),12*(x(t)+y(t))), \
    Eq(Derivative(y(t),t,2),12*x(t)+10*y(t)))
result = dsolve(eq)
print("ODEs-result",end=" ")
print(result)

                            #Matrix
from sympy.matrices import Matrix
x = symbols("x")
y = symbols("y")
result = sympy.linsolve([Eq(x-y,1),Eq(x+y,1)],(x,y))
print("linsolve",end=" ")
print(result)
result = sympy.nonlinsolve([Eq(x**2-y,1),Eq(x+y**2,3)],(x,y))
print("nonsolve",end=" ")
print(result)
