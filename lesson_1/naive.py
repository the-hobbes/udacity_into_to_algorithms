'''
  performs multiplication of two numbers.
  - much slower than russian.py
'''

def naive(a, b):
  # ab = xy + z
    x = a
    y = b
    z = 0
    while x > 0:
      z = z + y
      x = x - 1
    return z

def time(a):
    # The number of steps it takes to execute naive(a, b)
    # as a function of a (runtime depends on a). 
    # a linear function of a. 
    steps = 0
    # your code here
    steps = (a * 2) + 3
    return steps

def main():
  # print naive(10, 5)
  # print naive(5, 1)
  # print naive(5, 5)
  # print naive(0, 70)
  # assert(300, naive(30, 10))
  print naive(63, 12)

  time(10)

if __name__ == '__main__':
  main()
