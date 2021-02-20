#The math equation for Fibonacci sequence is
#fib(n) = fib(n-1) + fib(n-2) for n > 2
def Fib(n):
    # Write your code here.
	a = 0
	b = 1
	if n == 1:
		return a
	elif n == 2:
		return b
	else:
		F = [a,b]
		if n == 2:
			return 1
		else:
			for i in range (2,n):
				c = a + b
				a = b
				b = c
				F.append(c)
			return c
Fib(6)


def Fibular(n):
	a = 0
	b = 1
	if n == 1:
		return a
	if n == 2:
		return b
	F = [0]
	for i in range(1,n-1):
		c = a + b
		a = b
		b = c
		#F.append(c)
	return c
Fibular(1)



#This here is =O(2^n) time and O(n)space
def getNthFib(n):
    # Write your code here.
	if n == 2:
		return 1
	elif n == 1:
		return 0
	else:
		return getNthFib(n-1) + getNthFib(n-2)
getNthFib(6)

#testing
def getNthFib(n):
    # Write your code here.
	if n == 2:
		return 1
	elif n == 1:
		return 0
	else:
		return getNthFib(n-1) + getNthFib(n-2)

# Tested below using 6 as n
		return 6-1        	      +              6-2
			     5             	  +               4
	   5-1       +       5-2      +     4-1       +       4-2
	    4        +        3       +      3        +        2
    4-1 +  4-2   + 	 3-1  + 3-2   +  3-1 + 3-2    +
     3  +   2	 +    2   +  1 	  +  [2  +  1     +        2]
 3-1 + 3-2
 [2  +  1 + 2    +   2    +  1    +   2  +  1     +        2]
   				2 + 1 + 2 + 2 + 1 + 2 + 1 + 2
			   2+2+2+2+2+1+1+1
			   2 = 1
			   1 = 0
			   1+1+1+1+1+0+0+0
			   1*5 = 5
			   #answer is then 5
			  #answer is 5 because 4 + 1 since 2 hit base

#This is how I see it after reading the prompt again.
F1 = 0, F2 = 1, and n = (n-1) + (n-2)
def fib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

#O(n) time and O(n) space

def getfib(n, mem = {1:0, 2:1}):
	if n in mem:
		return mem[n]
	else:
		mem[n] = getfib(n-1, mem) + getfib(n-2, mem)
		return mem[n]

#iterative approach
def gfib(n):
	lasttwo = [0,1]
	counter = 3
	while counter <= n:
		nextFib = lastTwo[0] + lastTwo[1]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = nextFib
		counter += 1
	return lastTwo[1] if n > 1 else lastTwo[0]
