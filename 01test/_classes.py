class Student(object):
    def __init__(self,name,score):
        self._name =name
        self._score =score
    def get_name(self):
        return self._name
    def set_name(self,name):
        self._name=name
    def print_score(self):
        print('%s:%s' % (self._name,self._score))

class Animal(object):
    def run(self):
        print("animal is running..")

class Cat(Animal):
    pass

class Dog(Animal):    
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Teacher(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
