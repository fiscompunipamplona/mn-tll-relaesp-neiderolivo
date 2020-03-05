import math as mt

x=float( input("ingrese la distancia a la que se encuentra el planeta (años luz): "))
v=float( input("ingrese el valor de la velocidad, recuerde que como es una fraccion de c no debe ser mayor a 1:"))
c=3e8 #m/s

ly=9.461e15  #a en metros.
di=x*ly# distancia en metros
ve=v*c  # velocidad en fraciones de c
#timpo de recorrido desde la tierra  

t1=di/ve   #segundos

#tiempo visto desde la nave 

t2=(t1-((v*di)/c))/(mt.sqrt(1-v**2))





print('el tiempo desde la tierra hasta el planeta es:', t1)
print ('el timpo desde el planeta hasta la tierra es:',t2)

