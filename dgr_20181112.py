Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> fhand = open('mbox.txt')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    fhand = open('mbox.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbox.txt'
>>> print(fhand)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(fhand)
NameError: name 'fhand' is not defined
>>> <_io.TextIOWrapper name='mbox.txt
' mode='r' encoding='UTF-8'>
SyntaxError: invalid syntax
>>> nano mbox.txt
SyntaxError: invalid syntax
>>> fhand = open('mbox.txt')
>>> print(fhand)
<_io.TextIOWrapper name='mbox.txt' mode='r' encoding='UTF-8'>
>>> stuff = 'Hello\nWorld!'
>>> stuff
'Hello\nWorld!'
>>> print(stuff)
Hello
World!
>>> stuff = 'X\nY'
>>> print(stuff)
X
Y
>>> len(stuff)
3
>>> xfile = open('mbox.txt')
>>> for cheese in xfile:
	print(cheese)

	
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008  

#Return-Path: <postmaster@collab.sakaiproject.org>  

#Date: Sat, 5 Jan 2008 09:12:18 -0500  

#To: source@collab.sakaiproject.org  

#From: stephen.marquard@uct.ac.za  

#Subject: [sakai] svncommit: r39772 -content/branches/  



#Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772  

>>> fhand = open('mbox.txt')
>>> count = 0
>>> for line in fhand:
	count = count + 1

	
>>> print('Line Count:', count)
Line Count: 8
>>> $python open.py
SyntaxError: invalid syntax
>>> $ python open.py
SyntaxError: invalid syntax
>>> fhand = open('mbox-short.txt')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    fhand = open('mbox-short.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbox-short.txt'
>>> fhand = open('mbox-short.txt')
>>> inp = fhand.read()
>>> print(len(inp))
119
>>> print(inp[:20])
#From: stephen.marqu
>>> fhand = open('mbax-short.txt')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    fhand = open('mbax-short.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbax-short.txt'
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	if line.startswith('From:'):
		print(line)

		
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	line = line.rstrip()
	if line.startwith('From:'):
		print(line)

		
Traceback (most recent call last):
  File "<pyshell#42>", line 3, in <module>
    if line.startwith('From:'):
AttributeError: 'str' object has no attribute 'startwith'
>>> fhand = open('mbox-short.txt')for line in fhand:
	line = line.rstrip()
	if line.startswith('From:'):
		print(line)
		
SyntaxError: invalid syntax
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	line = line.rstrip()
	if line.startswith('From:'):
		print(line)

		
>>> 
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	if line.startswith('From:'):
		print(line)

		
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	line = line.rstrip()
	if not line.startswith('From:')
	
SyntaxError: invalid syntax
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	line = line.rstrip()
	if not line.startswith('From:'):
		continue
	print(line)

	
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	line = line.rstrip()
	if not '@uct.ac.za' in line:
		continue
	print(line)

	
#From: stephen.marquard@uct.ac.za
>>> fname = input('Enter the ile name:')
Enter the ile name:mbox.txt
>>> fhand = opne(fname)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    fhand = opne(fname)
NameError: name 'opne' is not defined
>>> fname = input('Enter the file name:')
Enter the file name:mbox.txt
>>> fhand = open(fname)
>>> count = 0
>>> for line in fhand:
	if line.startswith('Subject:'):
		count = count + 1

		
>>> print('There were', count, 'subject lines in',fname)
There were 0 subject lines in mbox.txt
>>> name = input('Enter the file name:')
Enter the file name:mbox-short.txt
>>> fhand = open(fname)
>>> count = 0
>>> for line in fhand:
	if line.startswith('Subject:'):
		count = count + 1

		
>>> print('There were', count, 'subject lines in',fname)

There were 0 subject lines in mbox.txt
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
	line = line.rstrip()
	if line.startswith('From:'):
		print(line)

		
>>> name = input('Enter the file name:')
Enter the file name:mbox-short.txt
>>> fhand = open(fname)
>>> count = 0
>>> for line in fhand:
	if line.startswith('Subject:'):
		count = count + 1

		
>>> print('There were', count, 'subject lines in',fname)
There were 0 subject lines in mbox.txt
>>> 
