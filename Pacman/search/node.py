#node.py

class Node:

	ID = 0

	def __init__(self, state, parent, action, pathcost): #constructor
		#print state, parent, action, pathcost
		self.state = state
		self.parent = parent
		self.action = action
		self.pathcost = pathcost
		self.ID = Node.ID
		Node.ID = Node.ID + 1
		pass

	def __str__(self):
		if self.parent == None: #para prevenir el error del padre = null en el estado inicial
			id = None
		else:
			id	= self.parent.ID

		return str(self.ID) + " " + str(self.state)+ " " + str(id) + " " + str(self.action) + " " + str(self.pathcost)


if __name__ == "__main__": #test unitario
	n = Node((5,5), None, None, 0)
	n2 = Node((5,4), n, 'South', 1)
	n3 = Node((4,4), n2, 'West', 2)
	n4 = Node((4,5), n3, 'Nord', 3)
	print n