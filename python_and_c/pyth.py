#!/usr/bin/env python2.6

from sys import path
path.append('build/lib.linux-x86_64-2.6') 
import mod
print(dir(mod))
import math
from random import random
from time import time

#ZAD1
print('zad 1')
print 'wynik dodawania: ',mod.met(1,2,3)


#ZAD2
print('\nzad 2')
x=[4,9,15,20]
print(mod.malo(x,4))


#ZAD3
print('\nzad 3')
f=lambda x: (3-math.sin(x**2))/(1+x)
#print(mod.mc(f))


def montec(a,b,fun):
	n=10000
	li=0
	for i in range(n):
		x=random()*abs(b-a)+a
		y=random()
		if y<fun(x): li+=1
	return float(li)/n


start = time()
print 'w pythonie:', montec(0,6,f)
end=time()
print('czasw pythonie:',end-start)
		
start = time()
print 'w C:', mod.mc(10000,0,6)
end=time()
print('czas w C',end-start)





