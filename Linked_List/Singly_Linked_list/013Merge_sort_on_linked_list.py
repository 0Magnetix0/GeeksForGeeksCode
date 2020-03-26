def displaylinkedlist(node):
    curr_node = node
    while curr_node != None:
        print(curr_node.data, end = " ")
        curr_node = curr_node.next
    print()

def merge(node1,node2):
    head = None
    res = None
    while node1 != None and node2 != None:
        if node1.data <= node2.data:
            if head is None:
                head = node1
                res = head
                node1 = node1.next
            else:
                res.next = node1
                res = res.next
                node1 = node1.next
        else:
            if head is None:
                head = node2
                res = head
                node2 = node2.next
            else:
                res.next = node2
                res = res.next
                node2 = node2.next

    while node1 != None:
        if head is None:
            head = node1
            res = head
            node1 = node1.next
        else:
            res.next = node1
            res = res.next
            node1 = node1.next

    while node2 != None:
        if head is None:
            head = node2
            res = head
            node2 = node2.next
        else:
            res.next = node2
            res = res.next
            node2 = node2.next
    return head

def mergeSort(A):
    if A.next == None:
        return A
    elif A == None:
        return None
    curr_node = A
    count = 0
    while curr_node != None:
        count += 1
        curr_node = curr_node.next
    count //= 2
    curr_node = A
    temp_node = A
    while count != 0:
        count -= 1
        temp_node = curr_node
        curr_node = curr_node.next
    temp_node.next = None
    left = mergeSort(A)
    right = mergeSort(curr_node)
    return merge(left,right)

def insertAtBegining(A,data):
    point = Node(data)
    if A.head is None:
        A.head = point
        return ;
    point.next = A.head
    A.head = point

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end = " ")
            curr_node = curr_node.next
        print(' ')
        return

A = LinkedList()
l = list(map(int,input().split()))
for x in l:
    insertAtBegining(A,x)
head = mergeSort(A.head)
A.head = head
A.printlist()
