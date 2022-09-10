import scipy.integrate as integrate
import numpy as np

#一重积分的lambda表达法
result1 = integrate.quad(lambda x:x**2+np.exp(x),0,5)
print("result1",end=" ")
print(result1)


#一重积分的函数表达法
a,b,c = 10,5,5
ARG = (a,b,c)
def fun(x,a,b,c):
    return a*x*(x>5)+b*x*(x<4)+c*x*(4<=x<=5)

result2 = integrate.quad(fun,3,6,args=ARG)
print("result2",end=" ")
print(result2)


#多重积分
def fun2(x,y,z,t,a,b):
    return x*y*z*t*a+b

def bounds_x(*args):
    return [0,3]
def bounds_y(*args):
    return [0,3]
def bounds_z(*args):
    return [0,0.5]
def bounds_t(*args):
    return [0,3]

a,b = 5,5
ARG = (a,b)

result3 = integrate.nquad(fun2,[bounds_x,bounds_y,bounds_z,bounds_t],args=ARG)
print("result3",end=" ")
print(result3)
