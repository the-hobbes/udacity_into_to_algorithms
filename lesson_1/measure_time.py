'''
  measuring the time as a function of input.
  countdown(50) takes (10 * 2) + 1 + 1 + 1 = 23

  take as input n and calculate the number of steps (time units)
  it takes to generate an output.
'''

import math

def time(n):
    """ Return the number of steps 
    necessary to calculate
    `print countdown(n)`"""
    steps = 0
    # YOUR CODE HERE
    n = math.ceil(n / 5.0)
    steps = (n * 2) + 3
    return steps

def countdown(x):
    y = 0
    while x > 0: 
        x = x - 5 # x counts down by 5 each loop
        y = y + 1
    print y

print countdown(50)
print time(50)
