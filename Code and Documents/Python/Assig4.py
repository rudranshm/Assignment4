import random

R=random.random()
pi=3.1415
#Method1
P=(pi*((R/2)**2))/(pi*(R**2))
print("The first probability is :", P)
#Method2
P=(((2*pi)/3)*(R))/(2*pi*R)
print("The second probability is :", P)
#Method3
P=((R/2)/(R))
print("The third probability is :", P)
