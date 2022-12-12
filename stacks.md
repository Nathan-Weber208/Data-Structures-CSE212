[Back to Introduction](introduction.md)
# Stacks
## Introduction
A stack is a way to store data. Stack is a very good name for it becouse it can be considered like a stack of papers. It uses the Last in, first out method of storing and displaying its data. For example:
```python
fruits = []

# append() method to add elements
fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")
print(fruits)

# pop() method to remove elements
fruits.pop()
print(fruits)

```
```python
# After adding
['apple', 'banana', 'cherry']
# After one pop
['apple', 'banana']
```

Notice that the last one added ('cherry') was the first to be popped off.

Other manipulation methods can be found [Here](https://www.geeksforgeeks.org/stack-in-python/#:~:text=A%20stack%20is%20a%20linear,often%20called%20push%20and%20pop.)

## Complexity of Stacks
When you work with a stack, you are forced to play by the rules of "first-in last-out" these limitations are put in place for good reason. Let's look over each method and ponder why it works the way that it works


### The append() method 
The limitations of adding only to the top of the stack makes it so that the append() method only has a time complexity of ***O(1)***. There is no looking for a place to put the entry.

### The pop() method
The time complexity of simply taking the last entered result is ***O(1)***. pop() is not a search function when you are working with stacks.

## Problem to solve
You are given a list of people who signed up to an event in the form of a stack. you don't know how long it will be but only 12 people can be let in. If you were to just pop the list 12 times, you would get the 12 last people who signed up. you don't want this. you want the first 12 people who signed.

Download [this](stackproblem.py) python program and fix the partyinvite() function.

[Solution](stacksolution.py)


[Back to Introduction](introduction.md)