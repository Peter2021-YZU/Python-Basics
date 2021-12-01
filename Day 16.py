# A quick introduction to Python iterators iter and next

# use iter and next to iterate a tuple
tup = ("John", "Peter", "VJP")
it = iter(tup)
print(next(it))
print(next(it))
print(next(it))


# use iter and next to iterate a str
str = "Peter"
it = iter(str)
print(next(it))
print(next(it))

# use iter and next to iterate a set
mySet = {"John", "Peter", "VJP"}
it = iter(mySet)
print(next(it))
print(next(it))
print(next(it))