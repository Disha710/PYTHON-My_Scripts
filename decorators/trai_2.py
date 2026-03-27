import functools
import datetime

def logger(func):
  @functools.wraps(func)
  def wrapper(*args,**kwargs):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S:")
    print(f"[{timestamp}] calling {func.__name__}")
    result = func(*args,**kwargs)
    print(f"[{timestamp}] calling {func.__name__}")
    return result
  return wrapper
@logger
def add(a, b):
    return a + b

add(10, 20)