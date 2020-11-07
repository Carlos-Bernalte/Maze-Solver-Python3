#!/usr/bin/python3
# -- coding: utf-8 --

import time
from Node import Node

n = Node(1,1,(0,0),0,"E",1,1,1)
list =[]
set=set()

'''no se puede hacer una tupla que sea comun la variable, ya que sale error "UnboundLocalError: local variable 't' referenced before assignment"
para solucionarlo hay que poner el "return t" que aparece en test2()
en las tuplas no se puede eliminar items, lo que hace que no se puedan usar
las tuplas ademas no se ejecutan de forma eficaz con cien mil de iteraciones, puesto que tarda demasiado en realizarse la operacion
'''

def test():
    min=0
    max=0
    for i in range(10000000):
        time1=time.time()
        list.append(Node(i,1,(0,0),0,"E",1,1,1))
        time2=(time.time()-time1)
        if(i==0 or time2<min):
            min=time2
        if(time2>max ):
            max=time2
    print("lists \nmin:{0}, max:{1} ".format(min,max))


def test2():
    min=0
    max=0
    t=()
    for i in range(10000):#mas de esto no funciona bien
        time1=time.time()
        t1=(Node(i,1,(0,0),0,"E",1,1,1),)
        t = t + t1
        time2=(time.time()-time1)
        if(i==0 or time2<min):
            min=time2
        if(time2>max ):
            max=time2
    print("tuples: \nmin:{0}, max:{1} ".format(min,max))
    return t

def test3():
    min=0
    max=0
    for i in range(10000000):#cuando hay pocos elemtos en el set tarda menos que la lista, pero a medida que aumentan de tamaño este tarda mas
        time1=time.time()
        set.add(Node(i,1,(0,0),0,"E",1,1,1))
        time2=(time.time()-time1)
        if(i==0 or time2<min):
            min=time2
        if(time2>max ):
            max=time2
    print("sets: \nmin:{0}, max:{1}".format(min,max))

startTime= time.time()
test()
final=time.time()
total=final-startTime
print("tiempo total: {0}".format(total))
print("tiempo medio: {0}".format(total/10000000))

startTime= time.time()
t=test2()
final=time.time()
total=final-startTime
print("tiempo total: {0}".format(total))
print("tiempo medio: {0}".format(total/10000))

startTime= time.time()
test3()
final=time.time()
total=final-startTime
print("tiempo total: {0}".format(total))
print("tiempo medio: {0}".format(total/10000000))


'''conclusiones: aunque las diferencias entre probar con muchos elementos en sets o listas son algo variables, según la ejecucion del ordenador
(unas veces tarda mas los sets y a veces las listas), lo que siempre se comprueba es que el tiempo maximo de los sets siempre es mayor que
el tiempo maximo de las listas. Esto indica que cuanto mas elementos haya en la ejecucion mas diferencia va a existir entre sets y listas, 
mientras que si hay pocos elementos la diferencia es como mucho milesimas de segundo(infinitesimal).
Por lo tanto se realizara con listas.
'''