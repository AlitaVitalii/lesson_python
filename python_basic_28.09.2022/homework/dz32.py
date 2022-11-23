class Queue:
    name = None
    # elements = []

    def __init__(self, name=None, elements=None):
        self.name = name
        if elements is not None:
            self.elements = elements
        else:
            self.elements = []
    @property
    def is_empty(self):
        return len(self.elements) == 0

    def push(self, element):
        self.elements.append(element)

    def pop(self, default=None):
        return default if self.is_empty else self.elements.pop(-1)
        # if not self.is_empty():
        #     return self.elements.pop(0)
        # else:
        #     return default

    def __add__(self, other):
        return Queue(name=f"{self.name} + {other.name}", elements=self.elements + other.elements)

    def __str__(self):
        return str(self.elements)

    def __eq__(self, other):
        return len(self.elements) == len(other.elements)


queue01 = Queue(name='Реєстратура')
queue02 = Queue(name='Стоматолог')

queue01.push(10)
queue01.push(11)
queue01.push(12)
queue02.push(100500)
queue02.push(100501)
queue02.push(100502)

print('queue01:', queue01.name, queue01)
print('queue02:', queue02.name, queue02)

queue03 = queue01 + queue02

print('queue03', queue03.name, queue03)

print(queue01 == queue02)
#
# print(queue01.elements)
print(queue01.name)
print(queue01.pop())
print(queue01.pop())
print(queue01.pop())
print(queue01.pop())

if not queue02.is_empty:
    print(queue02.pop())
if not queue02.is_empty:
    print(queue02.pop())
if not queue02.is_empty:
    print(queue02.pop())
if not queue02.is_empty:
    print(queue02.pop())
print(queue02.pop('*'))

# # print(queue01.elements)
#
# print(queue02.name)
# print(queue02.pop())

