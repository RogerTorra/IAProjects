import sys
import os

class Conversor:

	def __init__(self):

		self.vars = 0
		self.weight = 0
		self.soft = []
		self.hard = []
		self.list_aux_vars = []
		self.n_vars = len(self.soft)
		self.count = 0

	def read(self,fname):
		f = open(fname,"r")
		if l[0] != 'c':
			l = line.split()
			if l[0] == 'p':
				self.vars = int(l[2])
				self.weight = l[4]
			if l[0] == self.weight:
				self.hard.append([int(i) for i in l[1:-1]])
			else:
				self.soft.append([[int(i) for i in l[1:-1]], int (l[0])])
		f.close()

	def softUnit(self):
		for c in self.soft:
			self.vars += 1
			aux = []
			aux.append( self.vars )

			for i in c[0]:
				aux.append( i )
 
			self.hard.append(aux)
			self.soft[self.n_vars][0] = -self.vars
			self.n_vars += 1
							

	def hardTern(self):

		for c in self.hard:

			if(len(c) > 3):
				tam_lista = len(c)-3
				self.list_aux_vars= []
				for tam in range(0,tam_lista):
				    self.vars +=1
				    self.list_aux_vars.append(self.vars)
				    self.list_aux_vars.append(-self.vars)
				list_aux =[]
				list_aux.append([c[0],c[1], self.list_aux_vars[0]])
				self.list_aux_vars.remove(self.list_aux_vars[0])
				for a in c[2:]:
				    list_aux1 = []
				    list_aux1.append(a)
				    for i in range(0,2):
							if(len(self.list_aux_vars) != 0):
								list_aux1.append(self.list_aux_vars[0])
								self.list_aux_vars.remove(self.list_aux_vars[0])
				    
				    list_aux.append(list_aux1)
				list_aux[-2].extend(list_aux[-1])
				list_aux.remove(list_aux[-1])
				self.hard.extend(list_aux)
				self.hard.remove(c)

				while True:
				    count = 0
				    for c in self.hard:
				        if(len(c) > 3):
				            count = 1
				            conversor.hardTern()
				    if(count == 0):
				        return False
            

	def write(self, fname):
		f= open(fname, "w")

		print >> f, "p cnf",self.vars,len(self.soft)+len(self.hard)
		
		for lits, w in self.soft:
			print >>f,lits,0
		for lits in self.hard:
			for lit in lits:
				print >>f, lit,
			print >>f,"0"
		f.close()
			
if __name__ == "__main__":
	conversor = Conversor()
	conversor.read(sys.argv[1])
	conversor.softUnit()
	conversor.hardTern()
	conversor.write("instance1-3.cnf")