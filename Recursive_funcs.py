#To find the mode
'''
mode = {}
def findmode(L,n = 0):
	if len(L) <= 0:
		return
	x = L.pop()
	try:
		if mode[x] >= 0:
			mode[x] += 1
	except KeyError:
			mode[x] = 1
	findmode(L,x)

findmode([1,1,1,1,2,3,3,4,5,6])
for i in mode.keys():
	print(i, ': ' ,mode[i])
'''

#Reversed Graph
'''
def reversethegraph(G):
	temp = []
	for i in G.keys():
		for j in range(len(G[i])):
			if G[i][j] not in temp:
				temp.append(G[i][j])
	dicc = {}
	for i in temp:
		tempy = []
		for j in G.keys():
			if i in G[j]:
				tempy.append(j)
		dicc[i] = tempy
	print(tempy)
	print(dicc)

reversethegraph({2:[1,2,3], 3:[1,2]})
'''

'''
#Find the factorial of a number

def fact(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n*fact(n-1)

print(fact(10))
'''

'''
#To find the sum of numbers upto N

def summ(n):
	if n == 0:
		return 0
	else:
		return n + summ(n-1)

print(summ(10))
'''

'''
#To multiply a and b

def mult(a,b):
	if b == 0:
		return 0
	else:
		return a + mult(a,b-1)

print(mult(10,20))
'''

'''
#To raise a number to a power

def power(a,b):
	if b == 0:
		return 1
	elif b > 0:
		return a * power(a,b-1)
	elif b < 0:
		b = -b
		return (1 / (a*power(a,b-1)))

print(power(9,-2))
print(1/81)
'''
'''
#To find the GCD

def gcd(x,y):
	if x % y == 0:
		return y
	else:
		return gcd(y,x%y)

print(gcd(20012,164922))
'''

'''
#Reverse a string

def revving(a,i = 1):
	b = len(a)
	if i == len(a):
		return a[b-i]
	else:
		return a[b-i] + revving(a,i+1)

print(revving('LOLO'))
'''

'''
#Reverse a word string

def revving_remastered(a, i=1):
	c = a.split()
	b = len(c)
	if i == len(c):
		return c[b-i]
	else:
		return c[b-i] + ' ' + revving_remastered(a,i+1)

print(revving_remastered("Aniket Pradhan is a rockstar"))
'''

'''
#elfish

def elfish(lis, word = 'elf'):
	if len(word) == 0:
		return True
	if word[0] in lis:
		return elfish(lis,word[1:])
	else:
		return False

choice = int(input())
listofwords = input()
if choice == 0:
	print(elfish(listofwords))
else:
	word = input()
	print(elfish(listofwords, word))
'''