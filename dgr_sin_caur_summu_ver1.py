Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> # -*- coding: utf-8 -*-
... from math import *
>>> #(1.) * (2) = (2.) - float * int = float
... #(1.) * (2.) = (2.) - float * float = float
... #Python 2.x
... #x = 1. * input("Lietotāj, lūdzu, ievadi argumentu (x): ")
... #Python 2.x
... x = float(raw_input("Lietotāj, lūdzu, ievadi argumentu (x): "))
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
NameError: name 'raw_input' is not defined
>>> 
KeyboardInterrupt
>>> x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
Lietotāj, lūdzu, ievadi argumentu (x): 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: 
>>>     #x = float(raw_input("Lietotāj, lūdzu, ievadi argumentu (x): "))
... #Python 3.x
... x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
Lietotāj, lūdzu, ievadi argumentu (x): 1.89
>>> y = sin(x)
>>> print("sin(%.2f) = %.2f"%(x,y))
sin(1.89) = 0.95
>>> a0 = (-1)**0*x**1/(1)
>>> s0 = a0
>>> print("a0 = %.2f s0 = %.2f"%(a0, s0))
a0 = 1.89 s0 = 1.89
>>> a1 = (-1)**1*x**3/(1*2*3)
>>> s1 = a0 + a1
>>> print("a1 = %.2f s1 = %.2f"%(a2,s2))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a2' is not defined
>>> print("a1 = %.2f s1 = %.2f"%(a2,s2))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a2' is not defined
>>> print("a1 = %.2f s1 = %.2f"%(a1, s1)
... 
... 
... a1 = (-1)**1*x**3/(1*2*3)
  File "<stdin>", line 4
    a1 = (-1)**1*x**3/(1*2*3)
     ^
SyntaxError: invalid syntax
>>> a1 = (-1)**1*x**3/(1*2*3)
>>> a1 = (-1)**1*x**3/(1*2*3)
>>> s1 = a0 + a1
>>> print("a1 = %.2f s1 = %.2f"%(a1, s1))
a1 = -1.13 s1 = 0.76
>>> a2 = (-1)**2*x**5/(1*2*3*4*5)
>>> s2 = a0 + a1 + a2
>>> print("a2 = %.2f s2 = %.2f"%(a2,s2))
a2 = 0.20 s2 = 0.97
>>> a3 = (-1)**3*x**7/(1*2*3*4*5*6*7)
>>> s3 = a0 + a1 + a2 + a3
>>> print("a3 = %.2f s3 = %.2

