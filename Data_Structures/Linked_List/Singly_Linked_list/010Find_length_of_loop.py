#User function Template for python3

'''
Structure of node

class Node:
    data=0
    next=None
    
    
def newNode(data):
    temp=Node()
    temp.data=data
    temp.next=None
    return temp
'''

def countNodesinLoop(head):
    curr_node = head
    next_node = curr_node.next
    while curr_node != next_node:
        if curr_node is None:
            return 0
        if next_node is None:
            return 0
        curr_node = curr_node.next
        next_node = next_node.next
        if next_node is None:
            return 0
        next_node = next_node.next
    count = 1
    next_node = next_node.next
    while next_node != curr_node:
        count += 1
        next_node = next_node.next
    return count



#{ 
#  Driver Code Starts
class Node:
    data=0
    next=None
    

    
def newNode(data):
    temp=Node()
    temp.data=data
    temp.next=None
    return temp
    
def insert(head,data):
    if(head==None):
        head=newNode(data)
    else:
        head.next=insert(head.next,data)
    return head

def makeLoop(head,x):
    curr=head
    last=head
    counter=0
    while(counter<x):
        
        curr=curr.next
        counter+=1
    while(last.next!=None):
        last=last.next
    last.next=curr
            
def main():
    testcases=int(input())
    
    while(testcases>0):
        head=Node()
        head=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        x=int(input())
        
        for i in arr:
            head=insert(head,i)
        
        if x!=0:
            makeLoop(head,x)

        
        print(countNodesinLoop(head))
        
        testcases-=1




if __name__=="__main__":
    main()
# } Driver Code Ends
