def partyinvite(stack,number):
    #return the first number of names in the stack

    # pop() names from the stack until the number of names is reached
    while len(stack) > number:
        stack.pop()

    return stack


# starting with a stack of names
names = []
names.append("John")
names.append("Mary")
names.append("Peter")
names.append("Paul")
names.append("James")
names.append("Jill")
names.append("Jack")
names.append("Jenny")
names.append("Jane")
names.append("Jen")
names.append("Jenifer")
names.append("George")
names.append("Fred")
names.append("Frank")
names.append("Freddy")
names.append('Derek')
names.append('Ricky')

print(partyinvite(names,12)) # ['John', 'Mary', 'Peter', 'Paul', 'James', 'Jill', 'Jack', 'Jenny', 'Jane', 'Jen', 'Jenifer', 'George']
