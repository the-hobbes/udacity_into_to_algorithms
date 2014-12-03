# Write a function, `count`
# that returns the units of time
# where each print statement is one unit of time
# and each evaluation of range also takes one unit of time

def count(n):
    # Your code here to count the units of time
    # it takes to execute clique

    # for the first print and the first range(n)
    constant_cost = 2 

    # for the number of times the range(j) is called
    inner_range = n

    # calculate the total cost of the inner loop print statement
    inner_loops = range(n)
    inner_total = sum(inner_loops) # eg 0 + 1 + 2 + 3

    return constant_cost + inner_range + inner_total

def clique(n):
    print "in a clique..."
    for j in range(n):
        for i in range(j):
            print i, "is friends with", j


# clique(4)
print count(4) # should be 12