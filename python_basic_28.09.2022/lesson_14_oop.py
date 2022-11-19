class Queue:
    name = None
    elements = []

    def __init__(self, name, elements=None):
        self.name = name
        if elements is not None:
            self.elements = elements

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop(0)


queue01 = Queue(name="Реєстратура")  # , elements=[42, 43])
queue02 = Queue(name="Стоматолог")

queue01.push(1)
queue01.push(2)
queue01.push(3)

queue02.push(100500)

print(queue01.name)
print(queue01.pop())
print(queue01.pop())
print(queue01.pop())

print(queue02.name)
print(queue01.pop())

print('------------------------1')

class Queue:
    name = None

    def __init__(self, name, elements=None):
        self.name = name
        if elements is not None:
            self.elements = elements
        else:
            self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop(0)

    def __str__(self):
        return str(self.elements)


queue01 = Queue(name="Реєстратура")  # , elements=[42, 43])
queue02 = Queue(name="Стоматолог")

queue01.push(1)
queue01.push(2)
queue01.push(3)

queue02.push(100500)

print("Queue01:", queue01)
print("Queue02:", queue02)

queue02.push(100501)
print("Queue02:", queue02)
queue02.pop()
print("Queue02:", queue02)

print('--------------------2')

class Queue:
    name = None

    def __init__(self, name, elements=None):
        self.name = name
        if elements is not None:
            self.elements = elements
        else:
            self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop(0)

    def __add__(self, other):
        return Queue(name=f'{self.name} + {other.name}', elements=self.elements + other.elements)

    def __str__(self):
        return str(self.elements)


queue01 = Queue(name="Реєстратура")  # , elements=[42, 43])
queue02 = Queue(name="Стоматолог")

queue01.push(1)
queue01.push(2)

queue02.push(100500)

queue03 = queue01 + queue02

print("Queue01:", queue01.name, queue01)
print("Queue02:", queue02.name, queue02)
print("Queue03:", queue03.name, queue03)

print('------------------------3')

class Queue:
    name = None

    def __init__(self, name, elements=None):
        self.name = name
        if elements is not None:
            self.elements = elements
        else:
            self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop(0)

    def __add__(self, other):
        return Queue(name=f'{self.name} + {other.name}', elements=self.elements + other.elements)

    def __eq__(self, other):
        return self.name == other.name and self.elements == other.elements

    def __str__(self):
        return str(self.elements)


queue01 = Queue(name="Реєстратура")  # , elements=[42, 43])
queue02 = Queue(name="Стоматолог")

queue01.push(1)
queue01.push(2)

queue02.push(1)
queue02.push(2)

print("Queue01:", queue01.name, queue01)
print("Queue02:", queue02.name, queue02)
print(queue01 == queue02)

print('-----------------------------4')


# def pop(self, default=None):
#     return default if self.is_empty() else self.elements.pop(0)
#     # if not self.is_empty():
#     #     return self.elements.pop(0)
#     # else:
#     #     return default

print('------------------------------5')

class Queue:
    name = None

    def __init__(self, name, elements=None):
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
        return default if self.is_empty else self.elements.pop(0)

    def __add__(self, other):
        return Queue(name=f'{self.name} + {other.name}', elements=self.elements + other.elements)

    def __eq__(self, other):
        return self.name == other.name and self.elements == other.elements

    def __str__(self):
        return str(self.elements)


queue01 = Queue(name="Реєстратура")  # , elements=[42, 43])


queue01.push(1)
queue01.push(2)

print(queue01.pop())
print(queue01.pop())

if not queue01.is_empty:
    print(queue01.pop())
else:
    print(f"The '{queue01.name}' queue is empty")

print(queue01.pop(default='*'))

print('---------------------------6')

class Color:
    red = 'червоний'
    yellow = 'жовтий'
    green = 'зелений'


color = input("Введіть колір: ")


if color == Color.red:
    print("Стій")
elif color == Color.yellow:
    print("Приготуйся")
elif color == Color.green:
    print("Іди")

print('-----------------------7')

