import math

def func1(x):
    a=abs(2+math.sin(2*x))
    return math.log(a)

def func2(x):
    a=abs(1+math.sin(2*x))
    return math.log(a)
    
for i in range(10,13):
    print('func1: ',i,'-> ',func1(i))
    print('func2: ',i,'-> ',0.5*func2(i))
    print()

print('==============')

def function1(x):
    a=abs(1/math.sin(x)-1/math.tan(x))
    return math.log(a)

def function2(x):
    a=abs(1/math.tan(x)-1/math.sin(x))
    return math.log(a)

for i in range(10,13):
    print('function1: ',i,'-> ',function1(i))
    print('function2: ',i,'-> ',function2(i))
    print()
