
class AnimalType:
  def __init__(self,name,type):
    self.name = name
    self.type = type
a = AnimalType('cat','domestic')
print(a.name, a.type)  


class Animal:
  kind = 'reptiles'
  def __init__(self,name):
    self.name = name
    print(self.name)
a = Animal('snake')
a1= Animal('cobra')
print(a.kind, a1.kind)


class Flower:
  def __init__(self,name):
    self.name = name
    self.colors={}
  def add_colors(self,colors):
    self.colors.items()
  
f1 = Flower('Rose')
f2 = Flower("Lily")
f1.colors['Rose']= 'red'
print(f1.colors)
print(f2.colors)


class Sub:
   def __init__(self):
     self.result = {}
   def minux(self,num,val):
     self.result[num -1] = val
     
   def minustwice(self,num,val):
     self.result[num] = val
     self.result[num-1] = val
     
     
s= Sub()
s.minux(5 ,9)
s.minustwice(5,8)
print(s.result)


     
class Test:
    def __init__(self, item):
        self.l1 = []
        self.__update(item)    #  calls __update (private backup)
    
    def update(self, item):
        for x in item:
            self.l1.append(x)
    
    __update = update          #backup saved BEFORE child can override it

class Childtest(Test):
    def update(self, k, v):    # overrides "update" but NOT "__update"
        for x in zip(k, v):
            self.l1.extend(x)

c = Childtest([2,3,4,5]) #without privat it would have asked for 2 argument
print(c.l1)
c.update([66],[77])
print(c.l1)
     
  


from dataclasses import dataclass

@dataclass
class Warehouse:
    tool: str
    dept: str
    total: int

w = Warehouse('knief', 'workshop', 20)
print(w.tool)


def square(num):
  for x in range(num):
    yield x**2
    
for y in square(5):
  print(y)
    
 
 
    
print(list(i**2 for i in range(10)))