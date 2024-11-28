class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=self.right=None

a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
a.left,a.right=b,c

print(a.val,a.left.val,a.right.val)