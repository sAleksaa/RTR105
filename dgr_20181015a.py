Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print(123)
123
>>> print(98.6)
98.6
>>> print('Hello world')
Hello world
>>> x = 12.2
>>> y = 14
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 12.2, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> x = 12.2
>>> y = 14
>>> x = 100
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> x1q3z9ocd = 35.0
>>> x1q3z9afd = 12.50
>>> x1q3p9afd = x1q3z9ocd * x1q3z9afd
>>> print(x1q3p9afd)
437.5
>>> a = 35.0
>>> b = 12.50
>>> c = a * b
>>> print(c)
437.5
>>> hours = 35.0
>>> rate = 12.50
>>> pay = hors * rate

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    pay = hors * rate
NameError: name 'hors' is not defined
>>> pay = hours *rate
>>> print(pay)
437.5
>>> x = 2
>>> x = x + 2
>>> print(x)
4
>>> x = 3.9 * x * (1-x)
>>> x = 0.6
>>> vars()
{'a': 35.0, 'c': 437.5, 'b': 12.5, '__builtins__': <module '__builtin__' (built-in)>, 'pay': 437.5, '__package__': None, 'hours': 35.0, 'x1q3z9afd': 12.5, 'rate': 12.5, 'x1q3p9afd': 437.5, 'x': 0.6, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> x = 0.6
>>> x = 3.9 * x * (1 - x)
>>> print(x)
0.936
>>> print(x)
0.936
>>> x = 0.936
>>> x = 3.9 * x * (1-x)
>>> print(x)
0.2336256
>>> xx = 2
>>> xx = xx + 2
>>> print(xx)
4
>>> yy = 440 * 12
>>> print(yy)
5280
>>> zz = yy / 1000
>>> print(zz)
5
>>> float(zz)
5.0
>>> integer(zz)

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    integer(zz)
NameError: name 'integer' is not defined
>>> x = 0.6
>>> x = 3.9 * x * (1-x)
>>> print(x)
0.936
>>> x = 3.9 * x * (1-x)
>>> print(x)
0.2336256
>>> jj = 23
>>> kk = jj % 5
>>> print(kk)
3
>>> print(4**3)
64
>>> x = 1 + 2 * 3 - 4 / 5 ** 6
>>> print(x)
7
>>> x = 1 + 2 ** 3 / 4 * 5
>>> print(x)
11
>>> ddd = 1 + 4
>>> print(ddd)
5
>>> eee = 'hello'+ 'there'
>>> print(eee)
hellothere
>>> eee = 'hello' + 'there'
>>> print(eee)
hellothere
>>> eee = 'hello ' + 'there'
>>> print(eee)
hello there
>>> eee = 'hello ' + 'there'
>>> eee = eee + 1

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    eee = eee + 1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type(eee)
<type 'str'>
>>> <class'str'>
SyntaxError: invalid syntax
>>> class'str'
SyntaxError: invalid syntax
>>> <class 'str'>
SyntaxError: invalid syntax
>>> type(eee)
<type 'str'>
>>> type('hello')
<type 'str'>
>>> type(1)
<type 'int'>
>>> xx = 1
>>> type(xx)
<type 'int'>
>>> temp = 98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> print(float(99) + 100)
199.0
>>> i = 42
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10 / 2)
5
>>> print(9 / 2)
4
>>> print (99 / 100)
0
>>> print (10.0 / 2.0)
5.0
>>> print(99.0 / 100/0)

Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    print(99.0 / 100/0)
ZeroDivisionError: float division by zero
>>> print(99.0 / 100.0)
0.99
>>> sval = '¹23'
>>> sval = '123'
>>> type(sval)
<type 'str'>
>>> print(sval + 1)

Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    print(sval + 1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival = int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival + 1)
124
>>> nsv = 'hello bob'
>>> niv = ins(nsv)

Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    niv = ins(nsv)
NameError: name 'ins' is not defined
>>> nam = input('Who are you? ')
Who are you? 

Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    nam = input('Who are you? ')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> print('Welcome' nam)
SyntaxError: invalid syntax
>>> nam = input('Who are you? ')
Who are you? nam

Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    nam = input('Who are you? ')
  File "<string>", line 1, in <module>
NameError: name 'nam' is not defined
>>> nam = input('Who are you? ')
Who are you? 

Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    nam = input('Who are you? ')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> file
<type 'file'>
>>> new file
SyntaxError: invalid syntax
>>> nam = input('WHo are you?' , usf)

Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    nam = input('WHo are you?' , usf)
NameError: name 'usf' is not defined
>>> nam = raw_input('Who are you? ')
Who are you? nam
>>> print('Welcome' nam)
SyntaxError: invalid syntax
>>> print('Welcome', nam)
('Welcome', 'nam')
>>> nam = raw_input('Who are you? ')
Who are you? chuck
>>> print('Welcome', nam)
('Welcome', 'chuck')
>>> x = 5
>>> if x  < 10
SyntaxError: invalid syntax
>>> if x < 10:
	print('Smaller')
	if x > 20:
		print('Bigger')

Smaller
>>> print('Finis')
Finis
>>> x = 5
>>> if x ==5 :
	print('Equals 5')

	
Equals 5
>>> if x > 4;
SyntaxError: invalid syntax
>>> if x > 4:
	print('Greater than 4')

	
Greater than 4
>>> if x>=5:
	print('Greater than or Equals 5')

	
Greater than or Equals 5
>>> if x < 6:
	print('Less than 6')

	
Less than 6
>>> if x<= 5:
	print('Less than or Equals 5')

	
Less than or Equals 5
>>> if x!= 6:
	print('Not equal 6')

	
Not equal 6
>>> x = 5
>>> print('Before 5')
Before 5
>>> if x == 5:
	print('ls 5')
	print('ls Still 5')
	print('Third 5')

	
ls 5
ls Still 5
Third 5
>>> print('Afterwards 5')
Afterwards 5
>>> print('Before 6')
Before 6
>>> if x == 6:
	print('ls 6')
	print('ls Still 6')
	print('Third 6')
	print('Afterwards 6')

	
>>> print('Afterwards 6')
Afterwards 6
>>> x = 5
>>> if x > 2:
	print('Bigger than 2')
	print('Still bigger')

	
Bigger than 2
Still bigger
>>> print('Done with 2')
Done with 2
>>> for i in range(5):
	print(i)
	if i > 2:
		print('Bigger than 2')

		
0
1
2
3
Bigger than 2
4
Bigger than 2
>>> print('Done with i', i)
('Done with i', 4)
>>> print('All Done')
All Done
>>> if x<2
SyntaxError: invalid syntax
>>> astr = 'Hello Bob'
>>> istr = int(astr)

Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    istr = int(astr)
ValueError: invalid literal for int() with base 10: 'Hello Bob'
>>> 


