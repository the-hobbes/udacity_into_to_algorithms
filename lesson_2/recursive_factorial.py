def factorial( n ):
  print n
  if n == 1:
    print "bottom of recursion"
    return 1
  return n * factorial( n - 1 )

result = factorial(5)