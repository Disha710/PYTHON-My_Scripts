def do_twice(func):
  def wrapper_do_twice():
    func()
    func()
  return wrapper_do_twice

#*args and **kwargs
def universal_decorator(func):
  def wrapper(*args, **kwargs):
    print("Arguments passed: {args}, {kwargs}")
    return func(*args, **kwargs)
  return wrapper

#returning value
def return_value_decorator(func):
    def wrapper(*args, **kwargs):
        print("Running...")
        result = func(*args, **kwargs)  
        return result 
    return wrapper   
  
#Preserving Identity (@functools.wraps)
import functools
def better_decorator(func):
   @functools.wraps(func)
   def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
   return wrapper
 
#The @repeat Decorator
def repeat(num):
  def decorator_repeat(func):
    @functools.wraps(func)
    def wrapper_repeat(*args, **kwargs):
      value = None
      for _ in range(num):
        value = func(*args, **kwargs)
      return value
    return wrapper_repeat
  return decorator_repeat





