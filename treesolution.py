class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
    # order the tree
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


   # recursivly print the whole tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()

   def find(self, data):
      if self.data == data:
         return self
      elif self.data > data:
         if self.left is None:
            return None
         else:
            return self.left.find(data)
      else:
         if self.right is None:
            return None
         else:
            return self.right.find(data)




# Use the insert method to add nodes
root = Node(25)
root.insert(16)
root.insert(4)
root.insert(17)
root.insert(37)
root.insert(3)



# test the find method
print(root.find(3).data)  # should print 3
print(root.find(4).data) # should print 4
print(root.find(17).data) # should print 17