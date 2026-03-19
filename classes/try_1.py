#######Classes#############
#Virtual Methods: All functions in a Python class are "virtual," meaning they can always be overridden by a child class.

print("......defining class &constructor....")
class Complex:
  def __init__(self,realpart,imagpart):
    self.r = realpart
    self.i = imagpart
x = Complex(3.4,-4.5)
print(x.r, x.i)

print("__classes and instancess-----")

class Dog:
  kind = 'canine' #class variable shared by all obj
  
  def __init__(self,name):
    self.name = name #instance var unique to each obj
    print(self.name)
    
d = Dog('frodo')
d1 = Dog("bob")
print(d.kind)
print(d1.kind)

class Dog:
  #self.tricks = [] #should not right it here
  def __init__ (self,name):
    self.name = name
    self.tricks = [] #new empty list
  def add_tricks(self,trick):
    self.tricks.append(trick)
    
d= Dog('hifi')
e = Dog('fi')
d.add_tricks('roll over')
e.add_tricks('play head')
print(d.tricks)
print(e.tricks)

print('------method calling------')
class Bag:
  def __init__(self):
    self.data = []
    
  def add(self,x):
    self.data.append(x)
    
  def addtwice(self,x):
    self.add(x)
    self.add(x)
b = Bag()
b.add(5)
b.addtwice(5)
print(b.data)



print('------private variable & inheritance-----')
print("__ Name Mangling__")
class Mapping:
  def __init__(self,iterable):
    self.item_list = []
    self.__update(iterable)
    
  def update(self, iterable):
    for item in iterable:
      self.item_list.append(item)
      
  __update = update #private copy of ori method
  
class MappingSubclass(Mapping):
  def update(self,keys,values):
    for item in zip(keys,values):
      self.item_list.append(item)
      
m = MappingSubclass([1,2,3,4])
print(m.item_list)
m.update(['x'],[1])
print(m.item_list)
   
print("...dataclass class is mostly a container for data a record...")

from dataclasses import dataclass
@dataclass
class Employee:
  name : str
  dept : str
  salary: int
e = Employee('john','computer lab', 1000)
print(e.dept)

print(".....generater. : yield....")
#yield doesnot end function as return it pauses the function and gives a value
def reverse(data):
  for index in range(len(data)-1,-1,-1):
    yield data[index] #runs only when iterated
for char in reverse('golf'):
  print(char)
  
print(".....generater. :expression....")

# if gnerater is very samll donot need expression () withh create generater

print((sum(i*i for i in range(10))))
    
