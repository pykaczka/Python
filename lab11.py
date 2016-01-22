#!/usr/bin/env python3

#ZAD1
print('\n')
print('zad 1\n')

import abc
class Calka(metaclass=abc.ABCMeta):	
	def __init__(self, a, b, k, fun):
		if not isinstance(a,(int,float)):
			raise TypeError
		if not isinstance(b,(int,float)):
			raise TypeError
		if not isinstance(k,int):
			raise TypeError
		else:
			self.a=a
			self.b=b
			self.k=k
			self.fun=fun

	@abc.abstractmethod
	def licz(self):
		pass
			
class trapez(Calka):
	def licz(self):
		dx=(self.b-self.a)/self.k
		tmp=0
		for i in range(self.k):
			tmp+=self.fun(self.a+i*dx)
		tmp+=(self.fun(self.a)+self.fun(self.b))/2
		tmp*=dx
		return tmp

print('trapezy')
fun1 = lambda x: x*3
fun2 = lambda x: x**2+6*x+4
c1=trapez(1,3,10,fun1)
c2=trapez(1,3,100,fun1)
print(c1.licz(),c2.licz())
c3=trapez(2,6,1000,fun2)
print(c3.licz())


class simson(Calka):
	def licz(self):
		tmp,tmp1=0,0
		dx=(self.b-self.a)/self.k
		for i in range(self.k):
			x=self.a+i*dx
			tmp1+=self.fun(x-dx/2)
			if i<self.k:
				tmp+=self.fun(x)
		tmp=dx/6*(self.fun(self.a)+self.fun(self.b) +2*tmp+4*tmp1)
		return tmp

print('simpson')
c1=simson(1,3,10,fun1)
c2=simson(1,3,100,fun1)
print(c1.licz(),c2.licz())
c3=simson(2,6,1000,fun2)
print(c3.licz())




#ZAD2
print('\nzad 2\n')

class Lista:
	def __init__(self,x=0):
		if not x:		
			self.lista=[]
		elif x.__class__ is Lista:
			self.lista=x.lista[:]
		elif x:
			x.sort()
			self.lista=x		
		else:
			raise TypeError
				
	def dodaj(self,x):
		self.lista.append(x)
		self.lista.sort()
		return self.lista

	def __len__(self):
		return len(self.lista)

	def __str__(self):
		tmp="["
		for i in self.lista:
			tmp += "%d " %i
		tmp += "]"
		return tmp
	
	def usun(self,x):
		tmp=[]
		for i in self.lista:
			if i!=x:
				tmp.append(i)
		self.lista=tmp
		return self.lista
	
	def licz(self,x):
		j=0
		for i in self.lista:
			if i==x: j+=1
		return j

	def index(self,x):
		tmp=[]
		for i in range(len(self.lista)):
			if self.lista[i]==x:
				tmp.append(i)
		return tmp

	def odwroc(self):
		tmp=[]
		N=len(self.lista)
		for i in range(N-1,-1,-1):
			tmp.append(self.lista[i])
		return tmp


l=[1,5,2,4,3,5,5]
l1=Lista(l)
print("l1:",l1)
print("usuwamy 4:",l1.usun(4))
print('liczba piatek:',l1.licz(5))
print('5 wystepuje na miescach listy:', l1.index(5))
print('dodajemy 3:',l1.dodaj(3))
print('odwrocona lista:',l1.odwroc())
