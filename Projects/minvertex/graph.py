import sys
import os
import subprocess
class Graph:

	def __init__(self):
			self.nodes = []
			self.edges = []
			
	def read(self,fname):
			f = open(fname,"r")
			for line in f:
				l = line.split()
				if l[0] == 'p':
					self.nodes = range(1, int(l[2])+1)
				elif l[0] == 'e':
					self.edges.append([int(l[1]),int(l[2])])
			f.close()

	def minvertexcover_to_maxsat(self):

		f = open("instance.wcnf", "w")
		
		T = len(self.nodes) + 1
		print >> f,'p wcnf',len(self.nodes),len(self.nodes) + len(self.edges), T

		for n in self.nodes:
			print >> f,1, -n ,0
		for e1,e2 in self.edges:
			print >> f,T, e1, e2 ,0
		f.close()

	def solution(self,output):
		for line in output:
			l = line.split()
			if l[0] == 'v':
				print ",".join([e for e in l[1:] if int(e) > 0])


if __name__ == "__main__":
		g = Graph()
		g.read(sys.argv[1])
		g.minvertexcover_to_maxsat()
		command = '../maxsat/maxsatz2009 instance.wcnf'		
		output = os.popen(command).readlines()
		g.solution(output)


