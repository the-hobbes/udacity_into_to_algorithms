#!/usr/bin/python

''' 
    Multiply all the numbers in a grid together. the
    grid is stored in a text file. 
    
    usage is:
    cat input.txt | ./divisible_by_5.py
'''

import sys

def naive_multiplier():
  cumulative = 0
  for line in sys.stdin:
    line = line.split()

    # convert every string to an int
    line_of_ints = map(int, line) 

    # use the reduce function to apply a function of two arguments cumulatively to the items of iterable
    # in this case the function is a lamda that multiplies each of the two numbers together
    # reduce(function, iterable) 
    cumulative += reduce(lambda left_num, right_num: left_num * right_num, line_of_ints)

  return cumulative % 5 == 0

print naive_multiplier()