
class Bank:
  interest_rate = 5.0
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
  def check_balance(self):
    print(f'{self.name} has balance {self.balance}')
    
b = Bank('Disha','1lakhs')
b.check_balance()

class Bank:
  def __init__(self, name, account_number):
      self.name = name
      self.account_number = account_number
      self.transactions = []  # instance variable 
  
  def deposit(self, amount):
      self.transactions.append(amount)
      return f"Deposited {amount}"
  
  def withdraw(self, amount):
      self.transactions.append(amount)
      return f"Withdrew {amount}"
  
  def show_history(self):
      return f"{self.name}'s transactions: {self.transactions}"

# Create objects and call methods
b1 = Bank('John', '12345')
b2 = Bank('sara', '67890')

b1.deposit(1000)
b1.withdraw(200)

b2.deposit(5000)

#private variable and inheritance
class Vehicle:
  def __init__(self,speed):
    self.__speed = speed
    
  def get_speed(self):
    return self.__speed
class Car(Vehicle):
  def __init__(self,speed,colors):
    super().__init__(speed)
    self.colors = colors
    
car = Car(120,'blue')
#print(car.__speed)
print(car.get_speed()) 



from dataclasses import dataclass
@dataclass
class Shop:
  name : str
  quantity : int
  status: str
s = Shop('Cafe',10, 'close')
print(s.status)

#generater
def even_number(n):
  for i in range(n):
    if i %2 == 0:
      yield i
      
print(list(even_number(100)))

#single expression

square = (x**2 for x in range(10))
print(list(square))