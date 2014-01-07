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

	def maxcut_to_maxsat(self):

		f = open("instance.wcnf", "w")
		
		T = len(self.nodes) + 1
		E = ( len(self.nodes) * (len(self.nodes)-1) ) / 2
		print >> f,'p wcnf',len(self.nodes),len(self.nodes) + (E - len(self.edges)), T

		for n in self.nodes:
			print >> f,1, n ,0
		complete = []
		for i in range(len(self.nodes) - 1):
			for j in range(i+1, len(self.nodes)):
				complete.append([self.nodes[i] , self.nodes[j]])
		for e1,e2 in complete:
			if [e1,e2] not in self.edges:
				if [e2,e1] not in self.edges:
					print >> f,T, -e1, -e2 ,0
		f.close()

	def solution(self,output):
		for line in output:
			l = line.split()
			if l[0] == 'v':
				print ",".join([e for e in l[1:] if int(e) > 0])


if __name__ == "__main__":
		g = Graph()
		g.read(sys.argv[1])
		g.maxcut_to_maxsat()
		command = '../maxsat/maxsatz2009 instance.wcnf'		
		output = os.popen(command).readlines()
		g.solution(output)


