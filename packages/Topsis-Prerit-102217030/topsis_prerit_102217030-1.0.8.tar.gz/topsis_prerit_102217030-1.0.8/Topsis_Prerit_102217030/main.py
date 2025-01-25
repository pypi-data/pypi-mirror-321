from Topsis_Prerit_102217030 import run # type: ignore
import os
import sys
import numpy as np
import argparse
import pandas as pd
# if __name__ == "__main__":
#     main()

def valid_operators(value):
    operators = value.split(',')  # Split by comma
    valid_ops = ['+', '-']
    for op in operators:
        if op not in valid_ops:
            raise argparse.ArgumentTypeError(f"Invalid operator: '{op}'. Allowed operators are {valid_ops}.")
    return operators

def valid_numbers(value):
    try:
        numbers = [float(num) for num in value.split(',')]
        return numbers
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid numbers. Provide a comma-separated list of numbers.")
    

args = sys.argv
data = args[1]
weights = valid_numbers(args[2])
impact = valid_operators(args[3])
output = args[4]

run(data,weights,impact,output)

def main():
    pass

