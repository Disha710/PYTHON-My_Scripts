#compound statement
# 1.if statement Conditional code inside only runs if the condition is met
age = 20

if age >= 18:
    print("You are an adult.")
    print("You can vote.")
else:
    print("You are a minor.")
    
#2 while statement repeats the code as long as the condition stays True.

count = 3

while count > 0:
    print(count)
    count -= 1  # If we don't change count, it loops forever!
print("Blast off!")


# 3 for statemnet  Looping through a collection

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(f"I love eating {x}s")

# one-line if statement: using : ;
#if condition treu run hello than run world
if True: print("Hello"); print("world")


#ternary
text = "Hello" if True else "world"
print(text)


# 4 Try It allows you to run code that might fail without crashing the whole program
'''
4 parts
try : try somethig
except : if fail do this error handling
else: if worked do something else  runs if no exceptions were raised
finaaly: Cleanup runs no ,atter what
'''
try:
    # 1. THE ATTEMPT
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    # 2. THE ERROR HANDLER (Specific)
    print("That wasn't a valid number!")
    
except ZeroDivisionError as e:
    print(".......inportant : as keyword")
#When you use the as keyword in an except block, Python creates a local variable to hold the error details. To prevent memory leaks (specifically "reference cycles"), Python deletes that variable the moment the except block finishes.


    print(f"Inside the block, e is: {e}")
    # 'e' exists here and we can use it.
else:
    # 3. THE SUCCESS PATH
    print(f"Success! The result is {result}")
finally:
    # 4. THE CLEANUP (Always runs)
    print("Closing all resources.")


#Advanced Feature: except* only works with python 3.11
'''
try:
    # Imagine a group of errors happened at once
    raise ExceptionGroup("Many things went wrong", [ValueError("Bad value"), TypeError("Bad type")])
except* ValueError:
    print("Handled the value error portion")
except* TypeError:
    print("Handled the type error portion")
    
    '''
    
    
  # 5 with statement : (Context Managers, working with files no need to close manualy)
  #__enter__ __exit__
with open("hello.txt", "w") as f:
    f.write("Hello!")
    
#multi item
with open("source.txt") as src, open("dest.txt", "w") as dest:
    content = src.read()
    dest.write(content)
    
#6 match statement : pattern matching

flag = False
match (100, 200):
   case (100, 300):  # Mismatch: 200 != 300
       print('Case 1')
   case (100, 200) if flag:  # Successful match, but guard fails
       print('Case 2')
   case (100, y):  # Matches and binds y to 200
       print(f'Case 3, y: {y}')
   case _:  # Pattern not attempted
       print('Case 4, I match anything!')
       
status = 404
found_msg = ""

match status:
    case 200 | 201:            # OR Pattern
        print("Success")
    case 400 as error:         # AS Pattern
        print(f"Bad Request: {error}")
    case 404 if not found_msg: # Guard
        print("Not Found")
    case _:                    # Wildcard (Irrefutable)
        print("Something else went wrong")

command = "move north"

match command.split():
    case ["quit"]:
        print("Goodbye!")
    case ["move", direction]:
        print(f"Character is moving {direction}")
    case ["get", item]:
        print(f"Picking up the {item}")
    case _:
        print("Unknown command!")
