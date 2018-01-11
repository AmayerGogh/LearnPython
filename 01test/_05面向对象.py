#-*- coding:utf-8 -*-
from  _classes  import Student,Cat,Dog,Teacher
from types import MethodType
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()



#继承&多态
dog = Dog()
dog.run()

cat = Cat()
cat.run()

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(dog)
run_twice(cat)

#获取对象信息
print(type(dog))

#实例  绑定属性
dog.gender ='man'
print(dog.gender)

def set_gender(self, gender): # 定义一个函数作为实例方法
    self.gender = gender
#实例绑定 方法
dog.set_gender =MethodType(set_gender,dog)
dog.set_gender('woman')
print(dog.gender)
#给所有的实例绑定方法
def set_score(self, score):
    self.score = score
Student.set_score = set_score

#限制绑定__slots__
s = Teacher() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
