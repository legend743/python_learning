class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def LinkedList():
    l = [int(ele) for ele in input("Enter space-separated integers: ").split()]
    head = None
    last_node = None
    
    for i in range(len(l)):
        new_node = Node(l[i])
        if head is None:
            head = new_node
        else:
            current = head
            while current.next is not None:
                current = current.next
            current.next = new_node
            last_node = current
    
    return head, last_node

head, last_node = LinkedList()

def printl(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next

printl(head)

def lastLinked(head):
    current = head
    if current is None:
        return None
    else:
        while current is not None:
            last_node = current
            current = current.next
    print(last_node.data, "this is the last element of the linked list")

lastLinked(head)

def add_new_node(head, last_node):
    print(last_node.data, "this is the last node value")
    n = int(input("Enter new node: "))
    new_node = Node(n)
    last_node.next = new_node
    last_node = new_node  # Update the last_node variable
    print(new_node.data, "this is the new node")
    return head, last_node

head, last_node = add_new_node(head, last_node)
printl(head)
