class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

Root = Node('root')

Asia = Node('asia')
Africa = Node('africa')

Root.left = Asia
Root.right = Africa

India = Node('india')
bhutan = Node('bhutan')
Chad = Node('chad')
somalia = Node('somalia')

Asia.left = India
Asia.right = bhutan

Africa.left=Chad
Africa.right=somalia

maha=Node('maharashtra')
guj=Node('gujarat')

India.left = maha
India.right = guj

####################
##Depth-First ALGO##
####################

def preOrderTraversal(rootnode):
  if not rootnode:
    return
  print(rootnode.data)
  preOrderTraversal(rootnode.left)
  preOrderTraversal(rootnode.right)

#preOrderTraversal(Root)

def postOrderTraversal(rootnode):
  if not rootnode:
    return
  preOrderTraversal(rootnode.left)
  preOrderTraversal(rootnode.right)
  print(rootnode.data)

#postOrderTraversal(Root)

def inOrderTraversal(rootnode):
  if not rootnode:
    return
  preOrderTraversal(rootnode.left)
  print(rootnode.data)
  preOrderTraversal(rootnode.right)

#inOrderTraversal(Root)

#####################
##Breadth-First ALGO#
#####################

from collections import deque

def levelOrderTraversal(rootnode):
  q = deque()
  q.append(rootnode)

  while len(q) != 0:

    popped = q.popleft()
    print(popped.data)
    if popped.left is not None:
      q.append(popped.left)
    if popped.right is not None:
      q.append(popped.right)

#levelOrderTraversal(Root)
  
  
  



  
