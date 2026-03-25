import argparse
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
    

# python first_trail.py 4 -> Output: 16
# python first_trail.py 4 -v -> Output: The square of 4 equals 16 (Mode: fast)
# python first_trail.py 4 --mode slow -> Output: 16 (and internal mode is slow)
