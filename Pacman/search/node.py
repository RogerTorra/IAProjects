#node.py

class Node:

	ID = 0

	def __init__(self, state, parent, action, pathcost, depth): #constructor
		#print state, parent, action, pathcost
		self.state = state
		self.parent = parent
		self.action = action
		self.pathcost = pathcost
		self.depth = depth
		self.ID = Node.ID
		Node.ID = Node.ID + 1
		pass

	def path(self):
		# return [s,w,n] acciones que se han ejecutado hasta el nodo 
		stack = []
		node = self
		while node.parent != None:
			stack.append(node.action)
			node = node.parent
		stack.reverse()
		
		return stack

	def __str__(self):
		if self.parent == None: #para prevenir el error del padre = null en el estado inicial
			id = None
		else:
			id	= self.parent.ID

		return str(self.ID) + " " + str(self.state)+ " " + str(id) + " " + str(self.action) + " " + str(self.pathcost) + " " + str(self.depth)


if __name__ == "__main__": #test unitario
	n = Node((5,5), None, None, 0)
	n2 = Node((5,4), n, 'South', 1)
	n3 = Node((4,4), n2, 'West', 2)
	n4 = Node((4,5), n3, 'Nord', 3)
	print n4.path()