'''
  Create a Ring Graph. 
  - A ring graph is a graph where each node is connected to its neighbor, and
  the final node in the ring is connected to the first one.
'''


class RingGraph:


  def __init__(self, graph_size):
    # how many nodes in the graph?
    n = graph_size

    # make an empty graph
    a_ring = {}

    # add in the edges
    for i in range(n):
      self.make_link_(a_ring, i, (i + 1) % n) # %n to wrap to link end->start

    self.a_ring = a_ring

  def make_link_(self, G, node1, node2):
    print G, node1, node2
    '''
      Takes a graph and two nodes and establishes a connection between them.

      - Checks to see if the first node is in the graph, and if it isn't,
      creates an empty dictionary for that node. (does the same for the second
      node as well).
      - then it updats the graph, indicating that there is a connection between
      node 1 and node 2.

      Args:
            G, a graph of type dict
            node1, a node that needs to be linked to node 2
            node2, a node that needs to be linked to node 1
    '''
    if node1 not in G:
      G[node1] = {}
    (G[node1])[node2] = 1

    if node2 not in G:
      G[node2] = {}
    (G[node2])[node1] = 1

    return G

  def get_graph(self):
    return self.a_ring


def main():
  number_of_nodes = 5
  ring = RingGraph(number_of_nodes)

  a_ring = ring.get_graph()

  # tell us how many nodes are in the graph:
  print 'How many Nodes =>', len(a_ring)

  # tell us how many edges are in the graph
  # we / 2 because we are counting the edges twice (the edges from 1 to 2 and 
  #  2 to 1).
  print 'How many Edges =>', sum( [len(a_ring[node]) for node in a_ring.keys()] ) / 2

  # print the ring graph
  print 'The Graph =>', a_ring


if __name__ == '__main__':
  main()