class Node:
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None


root = Node(100)
node1 = Node(200)
node2 = Node(50)

root.right = node1
root.left = node2

node3 = Node(40)
node4 = Node(70)

node2.left = node3
node2.right = node4

node5 = Node(150)
node6 = Node(210)

node1.left = node5
node1.right = node6

node7 = Node(69)
node8 = Node(155)

node5.right = node8
node4.left = node7

#BST-ALGO

x = 155

def bst(Root, no):

  if Root != None :
    value = Root.data

  else :
    return f"{no} not found in tree"

  if value == no:
    return f"{no} found in tree"

  elif value < no:
    return bst(Root.right, no)

  elif value > no:
    return bst(Root.left, no)

print(bst(root, x))
