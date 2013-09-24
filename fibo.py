#!/usr/bin/python

def fib(n):
	a,b = 0,1
	while b<n:
        	print str(b) + ",", #Concatenamos 2 strings
        	a,b = b, a+b

if __name__ == '__main__':
	x = int(raw_input("Insert some integer: "))
	fib(x)
