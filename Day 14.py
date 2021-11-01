class myNode(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class doubleNode(object):
    def __init__(self, data, previous = None, next = None):
        self.data = data
        self.next = next
        self.previous = previous


a = myNode(3)
b = myNode(9)
c = myNode(0)
head = a
a.next = b
b.next = c

while head != None:
    print(head.data)
    head = head.next


a = doubleNode(10)
b = doubleNode(15)
c = doubleNode(2)
head = a
a.next = b
b.next = c
b.previous = a
c.previous = b
tail = c

while tail != None:
    print(tail.data)
    tail = tail.previous


