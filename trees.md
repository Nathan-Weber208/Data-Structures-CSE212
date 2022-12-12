[Back to Introduction](introduction.md)
# Trees
## Introduction
Unlike stacks and sets, trees are not yet baked into python. there is no handy method to just create a tree in one line and  start manipulating data. 

For the purpose of this tutorial though, thats a good thing. Im going to teach you to create a tree. That alone should teach all you have to know about them.

Simply put, a tree is a collection of independent ***nodes*** connected by ***edges***. If you look at any part of the tree, its just going to be a single node with a relationship to other nodes through these edges. 

### Step 1 - Create the Root
You need to create a class to hold a tree. 
```python
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def PrintTree(self):
      print(self.data)

root = Node(25)
root.PrintTree()
```
```python
25
```
Above, Ive given the root just one ability, to print itself.
If you run the code it should just store 25 as node and spit it out when you call the PrintTree() method.

### Step 2 insert() function
Just like the other data structures, trees need a insert method. Put this into your Node class
```python
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
```

### Step 3 PrintTree() function
Now that you have more than one node, adjust the tree to print the whole thing. Since this is a ordered tree, print the left node first using recursion. Here is an example.
```python
#recursively print the whole tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
```

### Test it
Here are some lines you can use to test your tree:
```python
root = Node(25)
root.insert(16)
root.insert(4)
root.insert(17)
root.insert(37)
root.insert(3)
root.PrintTree()
```
```python
3
4
16
17
25
37
```
Notice that the tree spits out the nodes in order. Thats not just how the PrintTree function is built but also how insert is written. Trees have single handedly taught me about recursion. It is essential to understand how recursive programming works to manipulate trees.

## Big O Performance of Trees
There isn't much guesswork for what performance this particular tree has. We built it ourselves. 
Our ***insert*** function does more than just make a node on the end of the tree. It recursively finds a place for it. It approaches ***O(log n)*** because it splits the tree in half as it finds a place for the new node to insert.

## Problem to solve
Now that you've built a way to store values in a tree. Build a function to search for a specific node.

Download [this](treeproblem.py) python program and fix the root.find() function.

[Solution](treesolution.py)

[Back to Introduction](introduction.md)