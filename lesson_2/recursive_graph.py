from random import choice


def make_link(G, node1, node2):
  # see ring_network.py for an explination. 
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1

  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1

  return G

def makeG(G, free_nodes):
  if len(G) == 1:
    return G
  
  G1 = dict(makeG(G.items()[len(G) / 2:]))
  G2 = dict(makeG(G.items()[:len(G) / 2]))

  i1 = choice(G1.keys())
  i2 = choice(G2.keys())

  make_link(G, i1, i2)

def main():
  print makeG(n)

if __name__ == '__main__':
  main()

