class Student:
  school = 'ABC'
  def __init__(self,name):
    self.name = name
    
  def get_info(self):
    return f"{self.name} studies at {self.school}"

s1 = Student('john')
s2 = Student('Sau')
print(s1.get_info())
print(s2.get_info())



class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []  # instance variable - unique to each student
    
    def add_course(self, course):
        self.courses.append(course)
    
    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
    
    def get_schedule(self):
        return f"{self.name} is enrolled in: {self.courses}"
      
s1 = Student('Alice', '101')
s2 = Student('Bob', '102')

s1.add_course('Math')
s1.add_course('Physics')

s2.add_course('Biology')
s2.add_course('Chemistry')

print(s1.get_schedule())
print(s2.get_schedule()) 

s1.drop_course('Math')
print(s1.get_schedule()) 

#inheritance
class CellPhone:
  def __init__(self,brand,name):
    self.brand = brand
    self.name = name
  def info(self,number) :
    return f'{self.name} is using {self.brand} with {number}'
class SmartPhone(CellPhone):
  def __init__(self,brand,name,model):
    super().__init__(brand, name)
    self.model = model
  def info_smart(self, number):
    return f'{self.name} is using {self.brand} model {self.model} with {number}'
  
s1 = SmartPhone("iphone","Me","asy45")
print(s1.info(100))
  

#creating instance variable
class Student:
  def __init__(self,name):
    self.name = name
    self.marks = []
  def marks(self,marks):
    result = marks/10
    self.marks.append(result)

from dataclasses import dataclass
@dataclass
class Data:
  name : str
  place : str
  status: str
d = Data('Disha','Bangalore', 'married')
print(d.name)



#genrater
def count(n):
  for i in range(n):
    yield i
    
for num in count(100):
  print(num)

#generater as exppresseion

print(sum(i**2 for i in range(10)))

# Inheritance with Encapsulation
class Vehicle:
  def __init__(self, speed):
    self.__speed = speed  # Private
  
  def get_speed(self):
    return self.__speed

class Car(Vehicle):
  def __init__(self, speed, color):
    super().__init__(speed)
    self.__color = color  # Private to child
  
  def info(self):
    return f"Car: {self.__color} color, Speed: {self.get_speed()} km/h"

car = Car(100, "Red")
print(car.info())