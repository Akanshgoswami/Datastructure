class Node:
    def __init__(self,data,name):
        self.data = data
        self.name = name
        self.next = None

class LinkedList :
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("Linked list is Empty")
            return
        else:
            temp= self.head

            while temp is not None:
                print(temp.data,temp.name)
                temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llistneq = LinkedList()

    llist.head = Node(1,"akansh")
    second = Node(2,"goswami")
    third = Node(3,"sumit")

    llist.head.next = second
    second.next= third

    # print(llist.head.data)
    llist.printList()
    # llistneq.printList()

