#User function Template for python3
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''
def display_linkedList(head):
    curr_node = head
    while curr_node is not None:
        print(curr_node.data, end = " ")
        curr_node = curr_node.next
    print()

def reverse_list(head):
    curr_node = head
    if curr_node.next == None:
        curr_node.next = None
        return curr_node
    next_node = curr_node.next
    curr_node.next = None
    while next_node is not None:
        temp = next_node
        next_node = next_node.next
        temp.next = curr_node
        curr_node = temp
    return curr_node

def compare_linked_lists(head1,head2):
    curr_node1 = head1
    curr_node2 = reverse_list(head2)
    while curr_node2 is not None:
        if curr_node1.data != curr_node2.data:
            break
        curr_node1 = curr_node1.next
        curr_node2 = curr_node2.next
    else:
        return 1
    return 0
        

def isPalindrome(head):
    curr_node = head
    count = 0
    while curr_node is not None:
        count += 1
        curr_node = curr_node.next
    if count == 1:
        return 1
    temp = count
    count //= 2
    curr_node = head
    while count != 0:
        curr_node = curr_node.next
        count -= 1
    if temp % 2 != 0:
        curr_node = curr_node.next
    return compare_linked_lists(head,curr_node)
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node 

# returns the size of linked list
def getSize(head):
    count = 0
    curr_node = head
    while curr_node:
        count +=1
        curr_node = curr_node.next
    return count

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        if isPalindrome(a.head):
            print(1)
        else:
            print(0)
# } Driver Code Ends
