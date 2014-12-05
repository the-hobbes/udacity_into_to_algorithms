'''
	A fully connected (complete) graph looks like a mesh network, and has the 
	appearance of a star. Each node is connected to each other node in the graph.

	Is it possible to determine the total number of edges in the graph, given the
	total number of nodes?
	- each node will have connections to each other node. Therefore the number of
	edges each node will have is one less than the total number of nodes, as a 
	node doesn't connect to itself.
	- we can thus say that the total number of nodes is ((n - 1) * n) / 2
	- we divide by 2 to account for the fact that we are counting each edge twice

	Runtime:
	- the runtime of this algorithm is BigTheta(n^2)
'''

def clique(n):
	# How many edges in a complete graph on n nodes?
	return ((n - 1) * n) / 2

assert clique(5) == 10
assert clique(9) == 36
assert clique(0) != 1