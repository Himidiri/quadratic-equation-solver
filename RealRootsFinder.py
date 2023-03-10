#program that gets the coefficients 𝑎, 𝑏 and 𝑐 of a quadratic equation 𝑎𝑥2 + 𝑏𝑥 +𝑐 = 0

import math

    #Get user inputs

a = int(input("Enter the coefficient of x² : "))
b = int(input("Enter the coefficient of x : "))
c = int(input("Enter the constant value : "))

    #Calculate Discriminant

dis = b**2 - 4*a*c 

    #Cheking Condition for Discriminant 
if dis > 0:
    roots = 2
    x1 = ((-b + math.sqrt(dis))/(2*a))
    x2 = ((-b - math.sqrt(dis))/(2*a))
    x1=int(x1)
    x2=int(x2)
    print("The discriminant is greater than zero -> There are two real distinct roots") #Output
    print("The roots of",int(a),"x² +",int(b),"x +",int(c),"= 0", "are",x2,"and",x1)

elif dis == 0:
    roots = 1
    x = (-b / (2*a))
    x=int(x)
    print("The discriminant is zero -> There are two real identical roots") #Output
    print("The roots of",int(a),"x²+",int(b),"x +",int(c),"= 0", "are",x,'and',x)
    
else:
    roots = 0
    print("The discriminant is less than zero -> There are no real roots") #Output
       
        
