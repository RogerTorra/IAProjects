#randomMaze.py	
import random
import sys

if __name__ == "__main__":	
	random.seed( int(sys.argv[1]) )
	#for i in range(random.randint(5,10)):
		#print "%"
	#	for i in range(random.randint(5,10)):
	#		print "%"

	#for i in range(10):
	#	print random.choice((1,20,33,4))
	rx = random.randint(5,25)
	ry = random.randint(5,25)
	pw = float(sys.argv[2])
	matrix = []
	matrix.append(['%']*rx)
	for x in range(ry-2):
		row = ['%']
		for j in range(rx-2):
			if random.random() <= pw:
				row.append('%')
			else:
				row.append(' ')
		row.append('%')
		matrix.append(row)
	matrix.append(['%']*rx)	
	matrix[ry-2][1] = "."
	matrix[1][rx-2] = "P"

	f = open("hola.lay","w")

	for row in matrix:
		print >>f, "".join(row)
	f.close()
	pass