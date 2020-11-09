#!/usr/bin/python3
# -- coding: utf-8 --

import time
from Node import Node

list =[]
set=set()


def test():
    min=0
    max=0
    for i in range(10000000):
        time1=time.time()
        list.append(Node(1,(0,0),0,"E",1,1,1))
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
    for i in range(10000):
        time1=time.time()
        t1=(Node(1,(0,0),0,"E",1,1,1),)
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
    for i in range(10000000):
        time1=time.time()
        set.add(Node(1,(0,0),0,"E",1,1,1))
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
