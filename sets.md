[Back to Introduction](introduction.md)
# Sets
## Introduction
Sets allow you to store multiple items in a single variable. There are some limitations to sets, however. first, they don't allow for duplicates. they cant be changed and they don't have any built in order. 

```python
# create the set
myset = {25, 64, 234}

```

### Manipulating sets
Unlike a stack, a set cannot be manipulated so easily. 

That being said, you can add to a set with the ***add()*** method.

Using the ***remove()*** method will pull from the set but you need to know what you are going to remove. calling a remove() on something that isn't in the set will raise and error.

```python
myset = {25, 64, 234}
addlist = [12,34,56,67,89]
for number in addlist:
    myset.add(number)

print(myset)

removelist = [64, 234]
for number in removelist:
    myset.remove(number)

print(myset)
```
```
{64, 89, 34, 67, 234, 12, 56, 25}
{89, 34, 67, 12, 56, 25}
```

Other manipulation methods can be found [Here](https://www.w3schools.com/python/python_sets_methods.asp)

## Big O performance
There are methods in python that can unify sets together. These methods, like .difference(), are the least time efficient. Unlike .remove() and .add() they require all numbers of the set to be seen. to compare a set to a stack is to see the advantage of having a more rigid storing system.
## Problem to Solve
You will vbe given 2 similar sets. Use the .difference() method to make a set of what those 2 sets dont have in common.
Down

Download [this](setproblem.py) python program and fix the setdifference() function.

[Solution](setsolution.py)


[Back to Introduction](introduction.md)