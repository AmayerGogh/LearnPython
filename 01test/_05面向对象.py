#-*- coding:utf-8 -*-
from  _classes  import Student,Cat,Dog,Teacher
from types import MethodType
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()



#�̳�&��̬
dog = Dog()
dog.run()

cat = Cat()
cat.run()

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(dog)
run_twice(cat)

#��ȡ������Ϣ
print(type(dog))

#ʵ��  ������
dog.gender ='man'
print(dog.gender)

def set_gender(self, gender): # ����һ��������Ϊʵ������
    self.gender = gender
#ʵ���� ����
dog.set_gender =MethodType(set_gender,dog)
dog.set_gender('woman')
print(dog.gender)
#�����е�ʵ���󶨷���
def set_score(self, score):
    self.score = score
Student.set_score = set_score

#���ư�__slots__
s = Teacher() # �����µ�ʵ��
s.name = 'Michael' # ������'name'
s.age = 25 # ������'age'
