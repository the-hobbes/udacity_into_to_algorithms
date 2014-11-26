'''
  this algorithms performs a multiplication of a and b
  by using bit shifts.
  - much faster than naive.py
'''

def russian(a, b):
  x = a
  y = b
  z = 0
  while x > 0:
    if x % 2 == 1: z = z + y # when x is odd, set z
    y = y << 1 # bit shift, equivalent to double y
    x = x >> 1 # bit shift, equivalent to subtract 1, then halve x
  return z

# the number of times the loop will run is the number of times
# it will take to bit shift x until it reaches 0. (subtract 1, then
# divide by 2). This is floor(log2a) + 1.

def main():
  print russian(10, 5)
  print russian(5, 1)
  print russian(5, 5)
  print russian(0, 70)
  assert(300, russian(30, 10))

if __name__ == '__main__':
  main()