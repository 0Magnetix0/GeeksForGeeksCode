# your task is to complete this function
# function should return index to the any valid peak element
def findMid(head):
    count = 0
    curr_node = head
    while curr_node is not None:
        count += 1
        curr_node = curr_node.next
    count //= 2
    curr_node = head
    temp_count = 0
    while temp_count != count:
        temp_count += 1
        curr_node = curr_node.next
    return curr_node




#{ 
#  Driver Code Starts
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        print(findMid(head).data)




# } Driver Code Ends
