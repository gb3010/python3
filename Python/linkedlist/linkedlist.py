#!/usr/bin/python3
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
	
class Llist:
	def __init__(self,head):
		self.head = None 
	
	def printnodes(self):
		head_pointer = self.head
		while head_pointer is not None:
			print(head_pointer.data)
			head_pointer = head_pointer.next

	def insertatbeginning(self,data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insertatend(self,data):
		last_node = Node(data)
		head_ptr_ins = self.head
		if self.head == None:
			self.head = last_node
		else:
			while head_ptr_ins:
				traverse_node = head_ptr_ins
				head_ptr_ins = head_ptr_ins.next
			
			traverse_node.next = last_node

	def insertatposition(self,data,position):
		new_node_insert = Node(data)
		counter = 1
		pointer = self.head


		while pointer.next is not None:
			

			if counter == position:
				new_node_insert.next = pointer.next
				pointer.next = new_node_insert
				break
		
			counter += 1
			pointer = pointer.next



n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

l1 = Llist(n1)

l1.head = n1
n1.next = n2
n2.next = n3 


l1.printnodes()
print()
l1.insertatbeginning(0)

l1.printnodes()

l1.insertatend(4)
print()
l1.printnodes()


l1.insertatposition(44,2)
print()
l1.printnodes()
