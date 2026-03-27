from my_decorator import do_twice
@do_twice
def say_hello():
  print("Hello")
say_hello()

#*args and **kwargs:allows function to work with many argument it takes
from my_decorator import universal_decorator
@universal_decorator
def greet(name, message = "Hi"):
  print(f"{message}, {name}")
greet("Tom", message="Welcome")

#retruning value
from my_decorator import return_value_decorator
@return_value_decorator
def add(a, b,c= 5):
    return a + b+c
print(add(5, 10)) 

#func.tool : Preserving Identity
#When you decorate a function, you are technically replacing it with the "wrapper" function defined inside your decorator. This causes the original function to "lose its identity"
#this preserve __name__, __doc__ etc
from my_decorator import better_decorator
@better_decorator
def secret_function():
    """This is a secret."""
    pass
print(secret_function.__name__)
print(secret_function.__doc__)

#@repeat
from my_decorator import repeat
@repeat(num=5)
def greet(name):
    print(f"Hello {name}")

greet("Disha` ")

print("decortor inside the class....")
class Calculator:
  @return_value_decorator
  def add(self,a,b):
    return a+b
  
calc = Calculator()
print(calc.add(4,9))

#Decorating the whole class
from dataclasses import dataclass
@dataclass
class User:
  username : str
  email : str
  #dataclas automatically write __init__ for us
u = User("Disha","@gmail.com")
print(u)

#In nesting decorator down recorater will execute first
def bold(func):
  def wrapper(*args,**kwargs):
    return f"<b>{func()}</b>"
  return wrapper
def italic(func):
  def wrapper(*args,**kwargs):
    return f"<i>{func()}</i>"
  return wrapper
@bold
@italic
def greet():
  return "This is me:)"
print(greet())


print("classes as decorater")
#use class instead of func using __call__ and __init__
class Countcalls:
  def __init__(self,func):
    self.func = func
    self.count = 0
    
  def __call__(self,*args,**kwargs):
    self.count +=1
    print(f"call number {self.count}")
    return self.func(*args, **kwargs)
  
@Countcalls
def say_bye():
  print("bye")
say_bye()