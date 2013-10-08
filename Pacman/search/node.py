#node.py

class Node:
	
	def __init__(self, state, parent, action, pathcost): #constructor
		#print state, parent, action, pathcost
		self.state = state
		self.parent = parent
		self.action = action
		self.pathcost = pathcost
		pass

	def __str__(self):
		return str(self.state)+ " " + str(self.parent) + " " + str(self.action) + " " + str(self.pathcost)
if __name__ == "__main__": 
	n = Node((5,5), None, None, 0)
	print n