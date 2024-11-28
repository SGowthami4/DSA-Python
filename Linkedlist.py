class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
        
    def __str__(self):
        return f"{self.data=} {self.next=}"

# Counting nodes
def count_nodes(head):
    count=0
    while head:
        head=head.next
        count+=1
    print("count",count)
    return count  

#Printing linkedList  
def printLL(head):
    while head:
        print(head.data,end="->")
        head=head.next

# Inserting an element at beginning
def insert_at_first(head,num):
    # node=Node(num)
    # node.next=head
    # return node
    return Node(num,head)

# Insert at last
def insert_at_last(head,num):
    node=Node(num)
    if not head:
        return node
    ptr=head
    while ptr.next:
        ptr=ptr.next
    ptr.next=node
    return head


head=Node(1,Node(2,Node(3,Node(4,Node(5)))))
count_nodes(head)
count_nodes(head.next)
# printLL(head)
head=insert_at_first(head,0)
# printLL(head)
insert_at_last(head,6)
printLL(head)
