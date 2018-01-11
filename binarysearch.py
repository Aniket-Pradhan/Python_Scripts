from timeit import *
def binsearch(a,item):
	a.sort()
	lb = 0
	ub = len(a)-1
	flag = 0
	while ub - lb != 1:
		mid = (lb+ub)//2
		if a[mid] == item:
			flag = 1
			break
		elif a[mid] < item:
			lb = mid
		else:
			ub = mid
	if flag == 1:
		return "Found"
	else:
		return "Not here"

if __name__ == "__main__":
	S = """
	"""
	B = """
	(binsearch(a,b))
	"""
	print(min(Timer(B,setup=S).repeat(10,100)))