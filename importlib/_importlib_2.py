#importlib makes us to understand how import works, understand how Python actually finds files
#gives you total control over how Python finds, opens, and reads libraries.
# importlib.metadata: what version, who wrote it
#importlib.resources:pen a picture or a config file 


print("Functions.......")
'''
1. importlib.import_module() *** mostly used
 pkg.mod
 uses ..mod to look in folders "above" your current one
 
2. importlib.__import__() 
This is the low-level engine.

3. importlib.invalidate_caches() 
 Calling this function forces Python to look at the hard drive again to find any brand-new files.

4. importlib.reload(module) 
This is very useful for developers.
Reload: This forces Python to re-read the file and update the functions without stopping the program.

'''
print("abc, abstract method")
#1. MetaPathFinder
#2. Loader
import sys
import importlib.abc #rule
from importlib.abc import MetaPathFinder, Loader



print("machinery...... ")
import importlib.machinery #Actual code
from importlib.machinery import ModuleSpec
# 1. The "Suffix" Lists (The File Extensions)
# This module provides lists of allowed file endings:
# SOURCE_SUFFIXES: .py' These are files you can read.
# BYTECODE_SUFFIXES:.pyc. These are compiled files.
# EXTENSION_SUFFIXES: These are "compiled" C/C++ 
# all_suffixes(): A quick way to get all of the above in one list.

# 2. The "Built-in" Importers
# Python has special function for code 
# BuiltinImporter: Handles things like sys or time 
# FrozenImporter: Handles "frozen" code (code packed into a single executable file, like an .exe).
# 3. The "Path" Specialists (How Python finds your files)
#     a.PathFinder:  It looks through your sys.path (the list of folders on your computer) to find where a module .
#     b.FileFinder: It is assigned to one specific folder and knows how to scan it for .py or .pyc files.
#     c. SourceFileLoader: It opens a .py file, reads the text, and turns it into a Python module.
# 4. How it all fits together (The "Path Hook")
#  this as a Plugin System.
# Normally, Python only knows how to look inside Folders.
# Using a "Path Hook," : look inside other things (like a .zip file database) as if they were normal folders.


print("util...... ")
#ready-made parts to help you build your own importer without starting from zero
import importlib.util #tool
#1.Path converter
#cache_from_source() find path from .py to .pyc
#source_from_cache() opposit
# 2."Spec"
# spec_from_file_location(name, path):
# module_from_spec(spec):
# 3. resolve_name() 
# 4.LazyLoader
itertools = importlib.import_module('itertools')


import sys
from importlib.abc import MetaPathFinder, Loader
from importlib.machinery import ModuleSpec

class _ModuleLoader(Loader):
    def exec_module(self, module):
        #  add a function to the module
        module.hello = lambda: "I am a module that doesn't exist on disk!"

# 2. The Finder: finds the module when you try to import it
class _ModuleFinder(MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        if fullname == "imaginary_module":
            # If the user asks for our specific name, return the "Spec" (the map)
            return ModuleSpec(fullname, _ModuleLoader())
        return None

# 3. Add Finder to Python's internal search list (sys.meta_path)
sys.meta_path.insert(0, _ModuleFinder())




