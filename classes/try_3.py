class Person:
  def __init__(self, name):
    self.name = name

class Person:
  def __init__(self, name,age):
    self.name = name
    self.age = age
    self.skills = []
  
  def add_skills(self,skill):
    self.skills.append(skill)
    
  def details(self):
    return f"{self.name} Age {self.age} skills: {self.skills}"
  
p = Person('me',30)
p1 = Person('you',25)

p1.add_skills('CAN')
p.add_skills('python')

print(p1.details())
print(p.details())



#private variable and inheritance
class BankAccount:
    def __init__(self, initial_balance):
        self.balance = 0
        self.__initialize(initial_balance)  # Uses private copy
    
    def initialize(self, amount):
        # Public method - can be overridden by subclass
        self.balance = amount
        print(f"Balance set to {amount}")
    
    __initialize = initialize  # Private copy protects __init__


class PremiumAccount(BankAccount):
    def initialize(self, amount):
        # Subclass changes behavior - adds bonus
        bonus = amount * 0.1
        self.balance = amount + bonus
        print(f"Balance set to {amount} + {bonus} bonus = {self.balance}")

from dataclasses import dataclass
@dataclass
class Result:
  name : str
  count : int
  result : bool

r = Result('ACC',100,False)
print(r.name)
print(r.result) 


def mult(n):
  for x in range(n):
    yield x*x
    
for y in mult(10):
  print(y)

