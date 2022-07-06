class Node:
    def __init__(self,data):
        self.next = None
        self.prev= None
        self.data=data

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print("The given previous node cannot be NULL")
            return
        new_node= Node(new_data)
        new_node.next=prev_node.next
        prev_node.next  = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev= new_node
    def append(self,new_data):
        new_node= Node(new_data)
        if self.head  is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
        return
    def printList(self,node):
        print("\n Traversal in forward direction")
        while node:
            print("{}".format(node.data))
            last = node
            node = node.next
        print("\n Traversal in reverse direction")
        while last:
            print("{}".format(last.data))
            last = last.prev

llist = DoublyLinkedList()

# llist.append(6)
for i in range(6):
    llist.push(i)
# llist.push(4)


llist.insertAfter(llist.head.next, 9)




print("created DLL is: ")
llist.printList(llist.head)


