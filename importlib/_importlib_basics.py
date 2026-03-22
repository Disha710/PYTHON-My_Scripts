#impotlib enables dynamic imports and manipulation of the importprocess
import importlib
import importlib.util
math_module = importlib.import_module('math')
print(math_module.sqrt(16))

#frequently used
# 1. importlib.import_module() import module using name
# 2. importlib.reload() reloads previously imported module
# 3. importlib.find_spec() find specification for given module name

random_module = importlib.import_module('random')
print(random_module.randint(1,10))
print("...reloading module..")

#print(importlib.reload(random_module))
print(importlib.util.find_spec("collections"))


#real example
print("......example...")
module_name = input("Enter the module to import")
module = importlib.import_module(module_name)
print(module.sqrt(16))
