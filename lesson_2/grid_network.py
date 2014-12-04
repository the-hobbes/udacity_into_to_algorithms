'''
  Create a Grid Graph.
  - In a grid, each node is connected to adjacent nodes in a grid format.

  Solves this question:
  how many edges, if we have 265 nodes arranged as a square?
  across: 16 - 1 edges on one row, so 15 * 16 = 240
  down: same amound, so 240 * 2 = 480

  More generally,
  - each side of a perfect square graph has sqrt(n) nodes
  - each side has sqrt(n) - 1 edges
  - 2n - 2 * sqrt(n)
'''
import math


class GridGraph:


  def __init__(self, graph_size):
    # how many nodes in the graph?
    n = graph_size

    # make an empty graph
    G = {}
    side = int(math.sqrt(n))

    # for each pair of nodes, i and j, in the graph
    for i in range(side):
      for j in range(side):
        # if the node isn't on the last now (bottom edge), make a downward link
        if i < side - 1: self.make_link_( G, (i, j), (i + 1, j) )
        # if the node isn't on the far right row (right edge), make a link to the right
        if j < side - 1: self.make_link_( G, (i, j), (j + 1, j) ) 

    self.graph = G

  def make_link_(self, G, node1, node2):
    # see ring_network.py for an explination. 
    if node1 not in G:
      G[node1] = {}
    (G[node1])[node2] = 1

    if node2 not in G:
      G[node2] = {}
    (G[node2])[node1] = 1

    return G

  def get_graph(self):
    return self.graph


def main():
  number_of_nodes = 256
  grid = GridGraph(number_of_nodes)
  a_grid = grid.get_graph()

  print 'Num Nodes =>', len(a_grid)
  print 'Num Edges =>', sum([len(a_grid[node]) for node in a_grid.keys()]) / 2
  print 'The Graph =>', a_grid

if __name__ == '__main__':
  main()