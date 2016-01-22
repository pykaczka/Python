#include <Python.h>
#include "fun.h"

//static PyObject *mod_met(PyObject *self){
//static PyObject *mod_met(PyObject *self, PyObject *args, PyObject *kw){
static PyObject *mod_met(PyObject *self, PyObject *args){
	int a=0,b=0,c=0;
	//PyObject *c;
	if(!PyArg_ParseTuple(args, "i|ii", &a, &b, &c)){ //jezeli do stringa wstawi sie | to po sa opcjonalne
		//docs.python.org/2/c-api/arg.html
		//docs.python.org/2/c-api/concrete.html
		//docs.python.org/2/c-api/object.html
		//docs.python.org/2/c-api/exceptions.html
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("i", a+b+c);
}

static PyObject *mod_malo(PyObject *self, PyObject *args){
	PyObject *pyTab;

	int roz;
	if(!PyArg_ParseTuple(args, "Oi", &pyTab, &roz)) return NULL;
	int i;
	long tab[roz];
	for(i=0;i<roz;i++) *(tab+i) = PyInt_AsLong(PyList_GetItem(pyTab,i));
	double sr=srednia(tab,roz);
	double med=mediana(tab,roz);
	
	return Py_BuildValue("f,f",sr,med);
}

static PyObject *mod_mc(PyObject *self, PyObject *args){
	int n;
	double a, b;
	if(!PyArg_ParseTuple(args, "iii", &n, &a, &b)) return NULL;
	double m = moca(n,a,b);
	return Py_BuildValue("f",m);
}


//tablica metod
static PyMethodDef mod_metody[]={
	{"met", (PyCFunction)mod_met, METH_VARARGS, "Funkcja ..."}, 
	{"malo", (PyCFunction)mod_malo, METH_VARARGS, "Funkcja ..."}, 
	{"mc", (PyCFunction)mod_mc, METH_VARARGS, "Funkcja ..."}, 
	//nazwa funkcja stosowana w Pythonie, adres funkcji , j.w. lub METH_KEYWORDS lub METH_NOARGS, lancuch dokumentacyjny
	{NULL, NULL, 0, NULL}	//wartownik
};

//funkcja inicjalizujaca
PyMODINIT_FUNC initmod(void){
	Py_InitModule3("mod", mod_metody, "Modul rozszerzajacy ...");
}
