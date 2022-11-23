class Stack:

    def __init__(self, elements=None):
        if elements is not None:
            self.elements = elements
        else:
            self.elements = []

    @property
    def is_empty(self):
        return len(self.elements) == 0

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop(-1)

    def clear(self):
        self.elements.clear()

    @property
    def size(self):
        return len(self.elements)

    def __str__(self):
        return str(self.elements)


stack01 = Stack()
stack02 = Stack()
stack01.push(1)
stack01.push(2)
stack01.push(3)
stack01.push(4)
stack01.push(5)

print('Розмір stack01:', stack01.size)
if not stack01.is_empty:
    print("stack01", stack01)

print('Розмір stack02:', stack02.size)
if not stack02.is_empty:
    print("stack02", stack02)


while not stack01.is_empty:
    pop_stack = stack01.pop()
    print(pop_stack)
    stack02.push(pop_stack)

print('Розмір stack01:', stack01.size)
if not stack01.is_empty:
    print("stack01", stack01)

print('Розмір stack02:', stack02.size)
if not stack02.is_empty:
    print("stack02", stack02)

print('\nвидалення всіх елементів стеку')
stack02.clear()
print('Розмір stack01:', stack01.size)
print('Розмір stack02:', stack02.size)


