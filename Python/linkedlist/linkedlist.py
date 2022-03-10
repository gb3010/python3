#!/usr/bin/python3
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
	
class Llist:
	def __init__(self,head):
		self.head = None 
	
	def printnodes(self):
		while self.head is not None:
			print(self.head.data)
			self.head = self.head.next 

	def insertatbeginning(self,data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insertatend(self,data):
		last_node = Node(data)
		if self.head == None:
			self.head = last_node
		else:
			while self.head:
				traverse_node = self.head
				self.head = self.head.next 
			
			traverse_node.next = last_node




n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

l1 = Llist(n1)

l1.head = n1
n1.next = n2
n2.next = n3 


#l1.printnodes()

l1.insertatbeginning(0)

l1.printnodes()

l1.insertatend(4)

l1.printnodes()
