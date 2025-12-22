graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E']
}
graph2 = {
    'A': ['B', 'C', 'F'],
    'B': ['D', 'G'],
    'C': ['E', 'H'],
    'D': ['I'],
    'E': ['B'],
    'F': [],
    'G': ['J', 'C'],
    'H': ['K'],
    'I': [],
    'J': ['F'],
    'K': ['A']
}

tests = [
    ('A', 'B'),   # True
    ('C', 'D'),   # False
    ('A', 'E')    # True:
]
tests2 = [
    ('A', 'E'),   # True
    ('A', 'K'),   # True
    ('G', 'I'),   # True
    ('C', 'J'),   # True
    ('K', 'D'),   # True
    ('F', 'Z'),   # False: 'Z' not in graph
    ('A', 'A'),   # True: start == end
    ('E', 'K'),   # True
]

def directed_traversal(start, end, graph, visited=None):
    if visited is None:
        visited = set()
    if start == end:
        return True
    if start in visited:
        return False
    visited.add(start)

    for v in graph.get(start, []):
        if v == end:
            return True
        if directed_traversal(v, end, graph, visited):
            return True

    return False

print('Graph 1 tests:')
for s, e in tests:
    result = directed_traversal(s, e, graph)
    print(f"{s} -> {e}: {result}")

print('\nGraph 2 tests:')
for s, e in tests2:
    result = directed_traversal(s, e, graph2)
    print(f"{s} -> {e}: {result}")

