class BaseSequence:
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

    def __add__(self, other):
        return self.__class__(name=f'{self.name} + {other.name}', elements=self.elements + other.elements)

    def __eq__(self, other):
        return self.name == other.name and self.elements == other.elements

    def __str__(self):
        return str(self.elements)


class Queue(BaseSequence):
    def pop(self, default=None):
        return default if self.is_empty else self.elements.pop(0)


class Stack(BaseSequence):

    def pop(self, default=None):
        return default if self.is_empty else self.elements.pop()


queue01 = Queue("Реєстратура", [1, 2, 3])
queue02 = Queue("Стоматолог", [4, 5, 6])

result = queue01 + queue02
print(type(result))
print(result.name, result)
print(result.pop())

print('----------------------------1')


class BaseSequence:
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
        print('push start')
        self.elements.append(element)
        print('push finish')

    def __add__(self, other):
        return self.__class__(name=f'{self.name} + {other.name}', elements=self.elements + other.elements)

    def __eq__(self, other):
        return self.name == other.name and self.elements == other.elements

    def __str__(self):
        return str(self.elements)


class Queue(BaseSequence):
    def pop(self, default=None):
        return default if self.is_empty else self.elements.pop(0)


class Stack(BaseSequence):

    def push(self, element):
        print("before push", self.elements)
        super().push(element)
        print("after push", self.elements)

    def pop(self, default=None):
        return default if self.is_empty else self.elements.pop()

st01 = Stack("Реєстратура", [1, 2, 3])
st01.push(4)

print('---------------------------3')

class BaseSequence:
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
        print('push start')
        self.elements.append(element)
        print('push finish')

    def __add__(self, other):
        return self.__class__(name=f'{self.name} + {other.name}', elements=self.elements + other.elements)

    def __eq__(self, other):
        return self.name == other.name and self.elements == other.elements

    def __str__(self):
        return str(self.elements)


class Queue(BaseSequence):
    def pop(self, default=None):
        return default if self.is_empty else self.elements.pop(0)


class Stack(BaseSequence):

    def push(self, element):
        print("before push", self.elements)
        super().push(element)
        print("after push", self.elements)

    def pop(self, default=None):
        return default if self.is_empty else self.elements.pop()

st01 = Stack("Реєстратура", [1, 2, 3])
st01.push(4)

print('-------------------------4')

class Car:
    foo = "hey"
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self._odometer = 0

    @property
    def odometer(self):
        print("asked odometer value at", self._odometer)
        return self._odometer

    @odometer.setter
    def odometer(self, value):
        if value >= self._odometer:
            prev = self._odometer
            self._odometer = value
            print(f"updated odometer value from {prev} to {value}")
        else:
            raise ValueError("Incorrect value!")
        # self._odometer = value if value > self._odometer else self._odometer


honda = Car(model='Honda Accord', year=1996)
honda.foo = "ho"

honda.odometer = 42
print(honda.odometer)

honda.odometer = 100500
print(honda.odometer)

honda.odometer = 0
print(honda.odometer)

print('-------------------5')

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self._odometer = 0

    def get_odometer(self):
        return self._odometer

    def set_odometer(self, value):
        self._odometer = value if value > self._odometer else self._odometer


honda = Car(model='Honda Accord', year=1996)

honda.set_odometer(42)
print(honda.get_odometer())

honda.set_odometer(100500)
print(honda.get_odometer())

honda.set_odometer(0)
print(honda.get_odometer())

print('---------------------------6')

class BaseSequence:
    name = None

    def __init__(self, name, elements=None):
        self.name = name
        if elements is not None:
            self._elements = elements
        else:
            self._elements = []

    @property
    def is_empty(self):
        return len(self._elements) == 0

    def push(self, element):
        self._elements.append(element)

    def __add__(self, other):
        return self.__class__(name=f'{self.name} + {other.name}', elements=self._elements + other._elements)

    def __eq__(self, other):
        return self.name == other.name and self._elements == other._elements

    def __str__(self):
        return str(self._elements)

    @classmethod
    def create_sequence(cls, name, elements):
        return cls(name, elements)


class Queue(BaseSequence):
    def pop(self, default=None):
        return default if self.is_empty else self._elements.pop(0)


class Stack(BaseSequence):

    def pop(self, default=None):
        return default if self.is_empty else self._elements.pop()

    @staticmethod
    def create_stack(name, elements):
        return Stack(name, elements)


st01 = Stack.create_sequence("Реєстратура", [1, 2])
print(st01)
qu02 = Queue.create_sequence("Стоматолог", [3, 4])
print(qu02)

st02 = Stack.create_stack("Рентген", [57, 58])
print(st02)