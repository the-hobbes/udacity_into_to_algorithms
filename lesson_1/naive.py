def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

def main():
  print naive(10, 5)
  print naive(5, 1)
  print naive(5, 5)
  print naive(0, 70)
  assert(300, naive(30, 10))

if __name__ == '__main__':
  main()