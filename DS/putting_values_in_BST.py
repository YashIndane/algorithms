class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

root = Node(None)


#putting values in BST
def put(Root, value):

  if Root.data == None:
    Root.data = value

  else:
    if Root.data <= value:
      if Root.right == None:
        Root.right = Node(value)
      else:
        put(Root.right, value)


    elif Root.data > value:
      if Root.left == None:
        Root.left = Node(value)
      else:
        put(Root.left, value)


put(root, 10)
put(root, 50)
put(root, 23)
put(root, 5)

print(root.__dict__)
