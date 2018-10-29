Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> n = 5
>>> while n > 0
SyntaxError: invalid syntax
>>> while > 0"
SyntaxError: invalid syntax
>>> while > 0:
	
SyntaxError: invalid syntax
>>> while n > 0:
	print(n)
	n = n - 1

	
5
4
3
2
1
>>> print('Blastoff!')
Blastoff!
>>> print(n)
0
>>> while True:
	line = input('>')
	if line == 'done':
		break
	print(line)
	print('Done!')

	
>

Done!
>

Done!
>

Done!
>while True:
while True:
Done!
>

Done!
>

Done!
>

Done!
>

Done!
>done
>>> while True:
	line = input('>')
	if line[0] == '#':
		continue
	if line == 'done':
		break
	print(line)

	
>print('Done!')
print('Done!')
>
Traceback (most recent call last):
  File "<pyshell#25>", line 3, in <module>
    if line[0] == '#':
IndexError: string index out of range
>>> 
>>> hile True:
	line = input('>')
	if line[0] == '#':
		continue
	if line == 'done':
		break
	print(line)
	
SyntaxError: invalid syntax
>>> while True:
	line = input('>')
	if line[0] == '#':
		continue
	if line == 'done':
		break
	print(line)
	print('Done!')

	
>
Traceback (most recent call last):
  File "<pyshell#30>", line 3, in <module>
    if line[0] == '#':
IndexError: string index out of range
>>> while True:
	line = input('>')
	if line[0] == '#':
		continue
	if line == 'done':
		break
	print(line)
print('Done!')
SyntaxError: invalid syntax
>>> 
>>> while True:
	line = input('>')
	if line[0] == '#':
		continue
	if line == 'done':
		break
	print(line)

	
>
Traceback (most recent call last):
  File "<pyshell#35>", line 3, in <module>
    if line[0] == '#':
IndexError: string index out of range
>>> while True:
	line = input('>')
	if line[0] == '#':
		continue
	if line == 'done':
		break
	print(line)
	print('Done!')

	
>#
>#
>done
>>> for i in [5, 4, 3, 2, 1]:
	print(i)
	print('Blastoff!')

	
5
Blastoff!
4
Blastoff!
3
Blastoff!
2
Blastoff!
1
Blastoff!
>>> or i in [5, 4, 3, 2, 1]:
	print(i)
	
print('Blastoff!')
SyntaxError: invalid syntax
>>> for i in [5, 4, 3, 2, 1]:
	print(i)

	
5
4
3
2
1
>>> print('Blastoff!')
Blastoff!
>>> for i in [5, 4, 3, 2, 1]:
	print(i)
print('Blastoff!')
SyntaxError: invalid syntax
>>> friend = ['Joseph', 'Glenn', 'Sally']
>>> for friend in friends:
	print('Happy New Year:', friend)

	
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    for friend in friends:
NameError: name 'friends' is not defined
>>> friends = ['Joseph', 'Glenn', 'Sally']
>>> for friend in friends:
	print('Happy New Year:', friend)
	
SyntaxError: multiple statements found while compiling a single statement
>>> riends = ['Joseph', 'Glenn', 'Sally']
>>> for friend in friends:
	print('Happy New Year:', friend)

	
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    for friend in friends:
NameError: name 'friends' is not defined
>>> friends = ['Joseph', 'Glenn', 'Sally']
>>> for friend in friends:
	print('Happy New Year:', friend)

	
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
>>> print('Done!')
Done!
>>> print('Before')
Before
>>> for thing in [9, 41, 12, 3, 74, 15]:
	print(thing)

	
9
41
12
3
74
15
>>> print('After')
After
>>> largest_so_far=-1
>>> print('Before', largest_so_far)
Before -1
>>> for the_num in [9, 41, 12, 3, 74, 15]:
	if the_num >ArithmeticError largest_so_far:
		
SyntaxError: invalid syntax
>>> largest so far=-1
SyntaxError: invalid syntax
>>> largest_so_far=-1
>>> print('Before', largest_so_far)
Before -1
>>> for the_num in [9, 41, 12, 3, 74, 15]:
	if the_num > largest_so_far:
		largest_so_far = the_num
	print(largest_so_far, the_num)

	
9 9
41 41
41 12
41 3
74 74
74 15
>>> print('After', largest_so_far)
After 74
>>> zork = 0
>>> print('Before', zork)
Before 0
>>> for thing in [9, 41, 12, 3, 74, 15]:
	zork = zork + 1
	print(zork, thing)
print('After', zork)
SyntaxError: invalid syntax
>>> for thing in [9, 41, 12, 3, 74, 15]:
	zork = zork + 1
	print(zork, thing)
	print ('After', zork)

	
1 9
After 1
2 41
After 2
3 12
After 3
4 3
After 4
5 74
After 5
6 15
After 6
>>> for thing in [9, 41, 12, 3, 74, 15]:
	zork = zork + 1
	print(zork, thing)

	
7 9
8 41
9 12
10 3
11 74
12 15
>>> print('After', zork)
After 12
>>> zork = 0
>>> print('Before', zork)
Before 0
>>> for thing in [9, 41, 12, 3, 74, 15]:
	zork = zork + 1
	print(zork, thing)

	
1 9
2 41
3 12
4 3
5 74
6 15
>>> print('After', zork)
After 6
>>> zork = 0
>>> print('Before', zork)
Before 0
>>> for thing in [9, 41, 12, 3, 74, 15]:
	zork = zork + thing
	print(zork, thing)

	
9 9
50 41
62 12
65 3
139 74
154 15
>>> print('After', zork)
After 154
>>> count = 0
>>> sum = 0
>>> print('Before', count, sum)
Before 0 0
>>> for value in [9, 41, 12, 3, 74, 15]:
	count = count + 1
	sum = sum + value
	print(count, sum, value)

	
1 9 9
2 50 41
3 62 12
4 65 3
5 139 74
6 154 15
>>> print('After', count, sum, sum / count)
After 6 154 25.666666666666668
>>> print('Before')
Before
>>> for value in [9, 41, 12, 3, 74, 15]:
	if value > 20:
		print('Large number', value)

		
Large number 41
Large number 74
>>> print('After')
After
>>> found = False
>>> print('Before', found)
Before False
>>> for value in [9, 41, 12, 3, 74, 15]:
	if value == 3:
		found = True
	print(found, value)

	
False 9
False 41
False 12
True 3
True 74
True 15
>>> print('After', found)
After True
>>> smallest_so_far = -1
>>> print('Before', smallest_so_far)
Before -1
>>> for the_num in [9, 41, 12, 3, 74, 15]:
	if the_num < smallest_so_far:
		smallest_so_far = the_num
	print(smallest_so_far, the num)
	
SyntaxError: invalid syntax
>>> or the_num in [9, 41, 12, 3, 74, 15]:
	if the_num < smallest_so_far:
		smallest_so_far = the_num
	print(smallest_so_far, the_num)
	
SyntaxError: invalid syntax
>>> for the_num in [9, 41, 12, 3, 74, 15]:
	if the_num < smallest_so_far:
		smallest_so_far = the_num
	print(smallest_so_far, the_num)

	
-1 9
-1 41
-1 12
-1 3
-1 74
-1 15
>>> print('After', smallest_so_far)
After -1
>>> smallest = None
>>> print('Before')
Before
>>> for value in [9, 41, 12, 3, 74, 15]:
	if smallest is None:
		smallest = value
	elif value < smallest:
		smallest = value
	print(smallest, value)

	
9 9
9 41
9 12
3 3
3 74
3 15
>>> print('After', smallest)
After 3
>>> 
