Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> x =5
>>> if x < 10
SyntaxError: invalid syntax
>>> if x <  10:
	print('Smaller')

	
Smaller
>>> if x > 20:
	print('Bigger')

	
>>> print('Finis')
Finis
>>> x == 5
True
>>> print('Equals 5')
Equals 5
>>> if x > 4:
	print('Greater than 4')

	
Greater than 4
>>> if x>= 5:
	print('Greater than or Equals 5')

	
Greater than or Equals 5
>>> if x < 6:
	print('Less than 6')

	
Less than 6
>>> if x <= 5:
	print('Less than or Equals 5')
	if x !=6 :
		print('Not equal 6')

		
Less than or Equals 5
Not equal 6
>>> x =5
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

	
>>> print('Afterwards 6')
Afterwards 6
>>> x = 5
>>> if x > 2:
	print('Bigger than 2')
	print('Still bugger')

	
Bigger than 2
Still bugger
>>> print('Done with 2')
Done with 2
>>> for i in range(5)
SyntaxError: invalid syntax
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
>>> x = 5
>>> if x > 2:
	print('Bigger than 2')
	print('Still bigger')
	print('Done with 2')

	
Bigger than 2
Still bigger
Done with 2
>>> x = 42
>>> if x > 1
SyntaxError: invalid syntax
>>> if x > 1:
	print('More than one')
	if x < 100
	
SyntaxError: invalid syntax
>>> if x < 100:
	print('Less than 100')

	
Less than 100
>>> print('All done')
All done
>>> x = 4
>>> if x > 2:
	print('Bigger')

	
Bigger
>>> else:
	
SyntaxError: invalid syntax
>>> if x > 2:
	print('Bigger')
	else:
		
SyntaxError: invalid syntax
>>> x = 4
>>> if x > 2:
	print('Bigger')
else:
	print('Smaller')

	
Bigger
>>> print('All done')
All done
>>> if x < 2:
	print('Small')
	elif x < 10:
		
SyntaxError: invalid syntax
>>> if x < 10:
	print('Medium')
else:
	print('LARGE')
print('All done')
SyntaxError: invalid syntax
>>> print('large')
large
>>> print('All done')
All done
>>> x = 0
>>> if x < 2:
	print('Small')
if x < 10:
	
SyntaxError: invalid syntax
>>> x = 0
>>> if x < 2:
	print('small')

	
small
>>> x = 0
>>> if x < 2:
	print('small')
elif x < 10:
	print ('Medium')
else:
	print('LARGE')
print('All done')
SyntaxError: invalid syntax
>>> 
>>> print('All done')
All done
>>> x = 5
>>> if x < 2:
	print('small')
elif x < 10:
	print('Medium')
else:
	print('LARGE')

	
Medium
>>> print('All done')
All done
>>> x = 20
>>> if x < 2:
	print('small')
elif x < 10:
	print('Medium')
else:
	print('LARGE')

LARGE
>>> print('All done')
All done
>>> x = 5
>>> if x < 2:
	print('small')
elif x < 10:
	print('Medium')

	
Medium
>>> print('All done')
All done
>>> if x < 2:
	print('Below 2')
elif x>=2:
	print('Two or more')
else:
	print('Something else')

	
Two or more
>>> if x <2:
	print('Below 2')
elif x < 20:
	print('Below 20')
elif x < 10:
	print('Below 10')
else:
	print('Something else')

	
Below 20
>>> if x <2:
	print('Small')
elif x < 10:
	print('Medium')
elif x < 20:
	print('Big')
elif x < 40:
	print('Large')
elif x < 100:
	print('Huge')
else:
	print('Ginormous')

	
Medium
>>> $ cat notry. py
SyntaxError: invalid syntax
>>> $cat notry.py
SyntaxError: invalid syntax
>>> astr = 'Hello Bob'
>>> istr = int(astr)

Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    istr = int(astr)
ValueError: invalid literal for int() with base 10: 'Hello Bob'
>>> try:
	istr = int(astr)
except:
	istr = -1

	
>>> print('First', istr)
('First', -1)
>>> astr = '123'
>>> try:
	istr = int(astr)
except:
	istr = -1

	
>>> print('Second', istr)
('Second', 123)
>>> astr = 'Bob'
>>> try:
	print('Hello')
	istr = int(astr)
	print('There')
except:
	istr = -1

	
Hello
>>> print('Done', istr)
('Done', -1)
>>> rawstr = input('Enter a number:')
Enter a number:42
>>> try:
	ival = int(rawstr)
except:
	ival = -1

	
>>> if ival > 0
SyntaxError: invalid syntax
>>> if ival > 0:
	print('Nice work')
else:
	print('Not a number')

	
Nice work
>>> 
