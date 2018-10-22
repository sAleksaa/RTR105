Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> def things():
	print('Hello')
	print('Fun')

	
>>> thing()

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    thing()
NameError: name 'thing' is not defined
>>> print('Zip')
Zip
>>> things()
Hello
Fun
>>> big=max('Hello world')
>>> print(big)
w
>>> tiny=min('Hello world')
>>> print(tiny)
 
>>> 
>>> def max(inp):
	blah
	blah
	for x in inp:
		blah
		blah

		
>>> print(float(99)/100)
0.99
>>> i=42
>>> type(i)
<type 'int'>
>>> f=float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(1+2*float(3)/4-5)
-2.5
>>> sval='123'
>>> type(sval)
<type 'str'>
>>> print(sval +1)

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(sval +1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival =int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival + 1)
124
>>> nsv = 'hello bob'
>>> niv = int(nsv)

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    niv = int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and I work all day.')
	ValueError: invalid literal for int() with base 10: 'hello bob'
	
SyntaxError: invalid syntax
>>> x = 5
>>> print('Hello')
Hello
>>> def print_lyrics():
	print("I'm a lumberjack, and I'm okay.')
	      
SyntaxError: EOL while scanning string literal
>>> def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and I work all day.')

	
>>> print('Yo')
Yo
>>> x = x + 2
>>> print(x)
7
>>> print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
>>> def greet(lang):
if lang == 'es':
	
  File "<pyshell#53>", line 2
    if lang == 'es':
     ^
IndentationError: expected an indented block
>>> def greet(lang):
	if lang == 'es':
		print('Hola')
	elif lang == 'fr':
		print('Bonjour')
	else:
		print('Hello')

		
>>> greet('en')
Hello
>>> greet('es')
Hola
>>> greet('fr')
Bonjour
>>> def greet():
	return "Hello"
print(greet(), "Glenn")
SyntaxError: invalid syntax
>>> 
>>> print

>>> def greet():
	return "Hello"

>>> print(greet(), "Glenn")
('Hello', 'Glenn')
>>> print(greet(), "Sally")
('Hello', 'Sally')
>>> print(greet('en'), 'Glenn')

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    print(greet('en'), 'Glenn')
TypeError: greet() takes no arguments (1 given)
>>> def greet(lang):
	if lang == 'es':
		return 'Hola'
	elif lang == 'fr':
		return 'Bonjour'
	else:
		return 'Hello'

	
>>> print(greet('en'), 'Glenn')
('Hello', 'Glenn')
>>> print(greet('es'), 'Sally')
('Hola', 'Sally')
>>> print(greet('fr'), 'Michael')
('Bonjour', 'Michael')
>>> def addtwo(a, b):
	added = a+b
	return added

>>> x = addtwo(3, 5)
>>> print(x)
8
>>> 
