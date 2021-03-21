def power(a,b):
    if a<=0.0:
        return 0.0
    else:
        result=1
        for i in range(int(b)):
            result=result*a
        return float(result)


def factorial(a):
    result=1
    for i in range(1,int(a+1)):
        result=result*i
    return float(result)    
        

def exponent(x):
    num=1
    index=1
    while index<100:
        num+=power(x,index)/factorial(index)
        index=index+1
    return float(num)    


    
def muchlat(a):
    if a<0:
        a=-a
    return a    
    

def Ln(x):
    if x<=0.0:
        return 0.0
    else:   
        Yn=x-1.0
        Yn1=Yn+2*((x-exponent(Yn))/(x+exponent(Yn)))
        while muchlat(Yn-Yn1)>0.001:
            Yn=Yn1
            Yn1=Yn+2*((x-exponent(Yn))/(x+exponent(Yn)))
        return float(Yn1)

    
def XtimesY (x,y):
    if x<=0.0:
        return 0.0
    else:
        return float(exponent(y*ln(x)))


def sqrt(x,y):
    if x==0.0 or y<=0.0:
        return 0.0
    else:
        return float(XtimesY(y,(1/x)))

def calculate(x):
    if x<=0.0:
        return 0.0
    else:
        num1=exponent(x)
        num2=XtimesY(7,x)
        num3=1/x
        num4=sqrt(x,x)
        resulte=num1*num2*num3*num4
        resulte=float('%0.6f' % resulte)
        return resulte
    