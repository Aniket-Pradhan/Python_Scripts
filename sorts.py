import copy

def bub(a):
	for i in range(len(a)):
		for j in range(len(a)-1):
			if a[j] > a[j+1]:
				t = a[j]
				a[j] = a[j+1]
				a[j+1] = t

def sel(a):
	for i in range(len(a)):
		minind = i
		for j in range(i,len(a)):
			if a[minind] > a[j]:
				minind = j
		a[i],a[minind] = a[minind],a[i]

def ins(a):
	count = 0
	for i in range(1,len(a)):
		j = i
		while j>0:
			if i < 4:
				count += 1
			if a[j] < a[j-1]:
				a[j],a[j-1] = a[j-1],a[j]
			j -= 1
		print(a)
	print("COUNT",count)

def merge(a):
	if len(a) > 1:
		mid = len(a)//2
		left = a[:mid]
		right = a[mid:]
		merge(left)
		merge(right)
		i = 0
		j = 0
		c = []
		while i < len(left) and j<len(right):
			if left[i] < right[j]:
				c.append(left[i])
				i += 1
			else:
				c.append(right[j])
				j += 1
		while i < len(left):
			c.append(left[i])
			i += 1
		while j < len(right):
			c.append(right[j])
			j += 1

if __name__ == "__main__":
	a = input()
	a = a.split()
	for i in range(len(a)):
		a[i] = int(a[i])
	b = a
	c = a
	d = a
	#bub(b)
	#sel(c)
	ins(d)
	#merge(a)
	#print(b,"BUB")
	#print(c,"SEL")
	print(d,"INS")
	#print(a,"MERGE")