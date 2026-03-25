#ArgumentParser : container for argument specification
import argparse
parser = argparse.ArgumentParser(
  prog = "Name", #bydefault it will be main file name eg usage : first_tray.py
  description = "What it does", ##only print --help
  epilog = 'text at the bottom of help' #only print --help
  #This is text that appears at the very bottom, after all the argument descriptions.
)


#example 2
parser = argparse.ArgumentParser(
    prog='SuperTool', # Custom name
    usage='%(prog)s [options] <input_file>', 
    # %(prog)s = supertool, [] = optional <>= mandatory argument
    description='A simple script to process your data.', # Intro text
    epilog='Need help?' # Footer text
)
parser.print_help()
print("Run this by python first_trial.py -h")


print("......Parents......")
# Create a base parser with shared settings
# add_help=False is required so we don't get two "-h" flags
base_parser = argparse.ArgumentParser(add_help=False)
base_parser.add_argument('--user', help='Login username')

# Create the actual parser and inherit from the base
final_parser = argparse.ArgumentParser(parents=[base_parser])
final_parser.add_argument('--action', help='Action to perform')

# This parser now has BOTH --user and --action
final_parser.print_help()


print("......formatter.....")
import textwrap

parser = argparse.ArgumentParser(
    prog='MyTool',
    formatter_class=argparse.RawDescriptionHelpFormatter, # Keeps formatting
    description=textwrap.dedent('''\
        Important Steps:
          1. Run this first
          2. Check the output
          3. Done!
        ''')
)
parser.print_help()

print("...... Prefix Characters.....")
# Allow both '-' and '+' as prefixes
parser = argparse.ArgumentParser(prefix_chars='-+')

# Now you can create a flag that uses '+'
parser.add_argument('+v', '++verbose', action='store_true')

from os import sys
print("...... fromfile_prefix_chars.....")
with open('args.txt', 'w', encoding=sys.getfilesystemencoding()) as fp:
    fp.write('-f\nbar')
parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
parser.add_argument('-f')
parser.parse_args(['-f', 'foo', '@args.txt'])

print("...... add_help.....")
parser = argparse.ArgumentParser(prog='PROG', add_help=False)
parser.add_argument('--foo', help='foo help')
parser.print_help()






print("... ArgumentParser.add_argument():input to ArgumentParser...")
# name or flag type(start with -), name is compulsory flag type is optional
print("..name or flags..")
parser.add_argument('filename') #name : compulsory
parser.add_argument('-c','--count') #optional

print("..ation:what to do..")
parser.add_argument('-v','--verbose', action = 'store_true')
#Verbose means "giving a lot of detail / extra information."

parser = argparse.ArgumentParser()

# 1. Positional argument (Required)
parser.add_argument('square', type=int, help='Display a square of a given number')

# 2. Optional flag (store_true)
parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')

# 3. Optional with choices and default
parser.add_argument('--mode', choices=['fast', 'slow'], default='fast', help='Set the processing speed')

args = parser.parse_args()

# Accessing the values
answer = args.square**2

if args.verbose:
    print(f"The square of {args.square} equals {answer} (Mode: {args.mode})")
else:
    print(answer)
    

# python script.py 4 -> Output: 16
# python script.py 4 -v -> Output: The square of 4 equals 16 (Mode: fast)
# python script.py 4 --mode slow -> Output: 16 (and internal mode is slow)


print("... ArgumentParser.parse_args(): runs the parser...")

args = parser.parse_args()
print(args.filename, args.count, args.verbose)

