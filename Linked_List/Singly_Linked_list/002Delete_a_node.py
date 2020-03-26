def delete_kth_Node(head,k):
    curr_node = head
    temp_node = None
    count = 1
    while count != k:
        count += 1
        temp_node = curr_node
        curr_node = curr_node.next
    if k == 1:
        return head.next
    temp_node.next = curr_node.next
    return head

def insertAtBegining(A,data):
    point = Node(data)
    point.next = A.head
    A.head = point

def insertAtEnd(A,data):
    point = Node(data)
    curr = A.head
    if curr is None:
        A.head = point
        return
    while curr.next is not None:
        curr = curr.next
    curr.next = point


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end = " ")
            curr_node = curr_node.next
        print(' ')

for _ in range(int(input())):
    l = list(map(int,input().split()))
    A = LinkedList()
    for x in l:
        insertAtBegining(A,x)
    A.printlist()





