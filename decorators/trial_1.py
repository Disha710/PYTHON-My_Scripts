import os
print("........calling function in argumentline obj: str,int : first class object")
def say_hello(name):
  return f'Hello {name}'

def be_awesome(name):
  return f'Yo {name}, together we are awesomes'

def greet_bob(greeter_func):
  return greeter_func("Bob") #say_hello() missing 1 

print(greet_bob(say_hello)) #say_hello is a function without ()
print(greet_bob(be_awesome)) #so only reference is passed so functon is not executing

print("......inner Functions.")
def parent():
  print("Printing from parent()")
  def first_child():
    print("Hi, I am Disha")
  def second_child():
    print("call me Sweety")
  first_child()
  second_child()
parent()#need to call this before calling inner function
  
def parent(num):
  def first_child():
    return "Hi, I am Disha"
  def second_child():
    return "call me Sweety"
  if num == 1:
    return first_child
  else:
    return second_child #without () 
p = parent(1)
print(p)
print(p())

print("......simple decorators.....")
def decorator(func):
  def wrapper():
    print("something is appening")
    func()
    print("end")
  return wrapper
def say_whee():
  print("Wheel")
  
say_whee = decorator(say_whee)
say_whee()

#adding Syntactic Sugar
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_whee():
    print("Whee!")

say_whee()