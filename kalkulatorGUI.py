#!/usr/bin/env python

import sys,os
from string import *
from Tkinter import *
import Image
from math import *
from time import *
from random import *
from Canvas import *
from scipy.integrate import quad
from scipy.optimize import leastsq
from scipy.optimize import bisect
import numpy as np
import matplotlib.pyplot as plt

def onclick1():
  pole.insert(END, "1")
def onclick2():
  pole.insert(END, "2")
def onclick3():
  pole.insert(END, "3")
def onclick4():
  pole.insert(END, "4")
def onclick5():
  pole.insert(END, "5")
def onclick6():
  pole.insert(END, "6")
def onclick7():
  pole.insert(END, "7")
def onclick8():
  pole.insert(END, "8")
def onclick9():
  pole.insert(END, "9")
def onclick0():
  pole.insert(END, "0")

def onclickpl():
  pole.insert(END, "+")
def onclickmin():
  pole.insert(END, "-")
def onclickmn():
  pole.insert(END, "*")
def onclickdzi():
  pole.insert(END, "/")
def onclickresz():
  pole.insert(END, "%")
def onclickpot():
  pole.insert(END, "**")
def onclicknl():
  pole.insert(END, "(")
def onclicknr():
  pole.insert(END, ")")
def onclickrow():
  wart=eval(pole.get())
  pole.delete(0,END)
  pole.insert(0, str(wart))

def onclickcalka():
  tmp=(pole.get()).split()
  a=eval(tmp[1])
  b=eval(tmp[2]) 
  x=np.arange(a,b, 0.1)
  y=lambda x: eval(tmp[0]) 
  tmp=quad(y,a,b)
  pole.delete(0,END)
  pole.insert(0, str(tmp))

def onclickzero():
	try:
		tmp=(pole.get()).split()
		a=eval(tmp[1])
		b=eval(tmp[2])
		if a<b: a,b=b,a
		x=np.arange(a,b)
		y=lambda x: eval(tmp[0]) 
		tmp=bisect(y,a,b)
		pole.delete(0,END)
		pole.insert(0, str(tmp))
	except ValueError:
		tmp="zly zakres"
		pole.delete(0,END)
		pole.insert(0, str(tmp))

def onclickRysuj():
  global foto
  tmp=(pole.get()).split()
  a=eval(tmp[1])
  b=eval(tmp[2])
  x=np.arange(a,b, 0.1)  
  y=eval(tmp[0])
  plt.plot(x,y)

  plt.savefig('wykr.png', dpi=50)
  Image.open('wykr.png').save('wykr.gif')
  foto=PhotoImage(file="wykr.gif")
  cv.create_image(0,0,anchor=NW,image=foto)

def plik():
	global foto
	pl=pole.get()
	x=[]
	y=[]
	with open(pl) as p:
		li=p.readlines()
		for i in li:
			tmp=i.split()
			x.append(eval(tmp[0]))
			y.append(eval(tmp[1]))
	tmp="wczytano"
	pole.delete(0,END)
	pole.insert(0, str(tmp))
	plt.plot(x,y)
	plt.savefig('wykr.png', dpi=50)
	Image.open('wykr.png').save('wykr.gif')
	foto=PhotoImage(file="wykr.gif")
	cv.create_image(0,0,anchor=NW,image=foto)


def cl():
  pole.delete(0,END)
  cv.delete('all')
  plt.clf()

def exit():
  plt.close()
  okno.destroy()

okno = Tk()
import tkFont
calcfont=tkFont.Font(font=("Courier", 10, "bold"))
ebg='#000033'
gadbg="#8AC007"
pole = Entry(okno)
pole.config(width=60, fg="white", bg=ebg, font=calcfont)
pole.grid(row=1, column=0, columnspan=8, pady=10)
button = Button(okno, text='1', command=onclick1, bg=gadbg, font=calcfont)
button.grid(row=2, column=0, sticky=EW)
button = Button(okno, text='2', command=onclick2, bg=gadbg, font=calcfont)
button.grid(row=2, column=1, sticky=EW)
button = Button(okno, text='3', command=onclick3, bg=gadbg, font=calcfont)
button.grid(row=2, column=2, sticky=EW)
button = Button(okno, text='4', command=onclick4, bg=gadbg, font=calcfont)
button.grid(row=3, column=0, sticky=EW)
button = Button(okno, text='5', command=onclick5, bg=gadbg, font=calcfont)
button.grid(row=3, column=1, sticky=EW)
button = Button(okno, text='6', command=onclick6, bg=gadbg, font=calcfont)
button.grid(row=3, column=2, sticky=EW)
button = Button(okno, text='7', command=onclick7, bg=gadbg, font=calcfont)
button.grid(row=4, column=0, sticky=EW)
button = Button(okno, text='8', command=onclick8, bg=gadbg, font=calcfont)
button.grid(row=4, column=1, sticky=EW)
button = Button(okno, text='9', command=onclick9, bg=gadbg, font=calcfont)
button.grid(row=4, column=2, sticky=EW)
button = Button(okno, text='0', command=onclick0, bg=gadbg, font=calcfont)
button.grid(row=5, column=0, sticky=EW)
button = Button(okno, text='calka', command=onclickcalka, bg=gadbg, font=calcfont)
button.grid(row=5, column=2, sticky=EW)
button = Button(okno, text='m. zerowe', command=onclickzero, bg=gadbg, font=calcfont)
button.grid(row=5, column=1, sticky=EW)

button = Button(okno, text='+', command=onclickpl, bg=gadbg, font=calcfont)
button.grid(row=2, column=4, sticky=EW)
button = Button(okno, text='-', command=onclickmin, bg=gadbg, font=calcfont)
button.grid(row=2, column=5, sticky=EW)
button = Button(okno, text='*', command=onclickmn, bg=gadbg, font=calcfont)
button.grid(row=2, column=6, sticky=EW)
button = Button(okno, text='/', command=onclickdzi, bg=gadbg, font=calcfont)
button.grid(row=3, column=4, sticky=EW)
button = Button(okno, text='%', command=onclickresz, bg=gadbg, font=calcfont)
button.grid(row=3, column=5, sticky=EW)
button = Button(okno, text='**', command=onclickpot, bg=gadbg, font=calcfont)
button.grid(row=3, column=6, sticky=EW)
button = Button(okno, text='(', command=onclicknl, bg=gadbg, font=calcfont)
button.grid(row=4, column=4, sticky=EW)
button = Button(okno, text=')', command=onclicknr, bg=gadbg, font=calcfont)
button.grid(row=4, column=5, sticky=EW)
button = Button(okno, text='=', command=onclickrow, bg=gadbg, font=calcfont)
button.grid(row=4, column=6, sticky=EW)

button = Button(okno, text='Rysuj', command=onclickRysuj, bg=gadbg, font=calcfont)
button.grid(row=6, column=2, sticky=EW)

button = Button(okno, text='exit', command=exit, bg=gadbg, font=calcfont)
button.grid(row=5, column=6, sticky=EW)
button = Button(okno, text='clear', command=cl, bg=gadbg, font=calcfont)
button.grid(row=5, column=5, sticky=EW)
button = Button(okno, text='plik', command=plik, bg=gadbg, font=calcfont)
button.grid(row=5, column=4, sticky=EW)



cv = Canvas(okno, width=400, height=300)
cv["background"]="white"
cv["borderwidth"]=0
cv.pack(expand=1,fill=BOTH)
cv.config()
cv.grid(row=10, column=0, columnspan=9)



okno.title('Kalkulator')
okno.mainloop()
