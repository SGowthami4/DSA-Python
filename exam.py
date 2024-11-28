def solve(num, k):
    # CODE HERE
  st=[]
  n=len(num)
  for i in range(len(num)):
    while st and k>0 and st[-1]>num[i]:
        st.pop()
        k=k-1
    st.append(num[i])
  while k>0:
    st.pop()
    k=k-1
  res="".join(st).lstrip('0')
  return res if res else "0"
num="1432219"
k=3
print(solve(num,k))

#Linkedlist-Partition List
class Node:
   def __init__(self,data,next=None):
      self.data=data
      self.next=next
def solve(head,x):
   l1=n1=Node(12)
   l2=n2=Node(123)
   curr=head
   while curr:
      if curr.data<x:
         l1.next=curr
         l1=l1.next
      else:
         l2.next=curr
         l2=l2.next
      curr=curr.next
   l2.next=None
   l1.next=n2.next
   return n1.next

head=Node(1,Node(4,Node(3,Node(2,Node(5,Node(2))))))


      