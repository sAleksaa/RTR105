import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import sin, linspace

def f(x):
    return sin(x)

x = linspace(0,4,11)
print(x)
#y = sin(x)
y = f(x)
print(y)

legend = []

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('$sin(x)$ funkcija un tās atvasinājumi')
plt.plot(x,y,'k')
legend.append('$sin(x)$ funkcija')

plt.plot(x,y,'go')
legend.append('$sin(x)$ funkcija (daži punkti)')

deltax = x[1] - x[0]
N = len(x)
derivative = []

for i in range(N):
    temp = (f(x[i] + deltax) - f(x[i])) / deltax
    derivative.append(temp)
    print(derivative)

plt.plot(x,derivative,'y')
legend.append('atvasinājums')

plt.plot(x,derivative,'ro')
legend.append('atvasinājums (daži punkti)')

derivative_through_array = []
for i in range(N-1):
    temp = (y[i+1] - y[i]) / (x[i+1] - x[i])
    derivative_through_array.append(temp)

plt.plot(x[0:N-1],derivative_through_array,'m')
legend.append('atvasinājums (izmantojot vērtības no masīva)')

plt.plot(x[0:N-1],derivative_through_array,'bo')
legend.append('atvasinājums (izmantojot vērtības no masīva; daži punkti)')
#print(plt.legend.__doc__)
plt.legend(legend, loc = 3)
plt.show()
