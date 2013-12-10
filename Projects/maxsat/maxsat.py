class maxsat:

	def alo(self,lits):
		self.hard.append(lits)
	def amo(self,lits):
		#self.hard.append([(-x,-y) for x in range(len(lits) -1) for y in range(i+1, len(lits))])
		for i in range(len(lits)):
			for j in range(i+1, len(lits)):
					self.hard.append([-lits[i],-lits[j]])
	def eo(self,lits):
		self.alo(lits)
		self.amo(lits)

	def toSat(self, fname):
		f = open(fname, "w")
		#header
		print "p cnf", self.nvar, len(self.soft) + len(self.hard)

		#soft
		for c, w in self.soft:
			for lit in c:
				print lit,
			print "0"

		#hard
		for c, w in self.hard:
			for lit in c:
				print lit,
			print "0"
		f.close()

