from importlib.machinery import FrozenImporter


graph = {
    'S': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'E'},
    'D': set(),
    'E': {'D'},
    'A': {'F'},
    'F': {'G'},
    'G': set(),
}

def goal_test_producer(nodes_checked):
    def goal_test(node):
        nodes_checked.append(node)
        return node=='G'
    return goal_test

def dfs_tree(graph, goal_test, start='S'):
    frontier = [start]
    while frontier:
        node = frontier.pop()
        if goal_test(node):
            return node
        frontier.extend(sorted(graph[node]))
    return None

def dfs_graph(graph, goal_test, start='S'):
    explored, frontier = set(), [start]
    while frontier:
        node = frontier.pop()
        if goal_test(node):
            return node
        explored.add(node)
        frontier.extend(sorted(graph[node] - explored - set(frontier)))
    return None

def bfs_tree(graph, goal_test, start='S'):
    # TODO Implement this
    # push it into the queue and pop out the starting and add the neighbours of it
    frontier = [start]
    while frontier:
        node = frontier.pop(0)
        if goal_test(node):
            return node
        # add each children into the frontier
        for x in sorted(graph[node]):
            # print(x, end="->")
            frontier.extend(x)
    return None        

def bfs_graph(graph, goal_test, start='S'):
    # TODO Implement this
    explored, frontier = set(), [start]
    while frontier:
        node = frontier.pop(0)
        if goal_test(node):
            return node
        # add each children into the frontier
        for x in sorted(graph[node]):
            if(x not in explored):
                explored.add(x)
                frontier.extend(x)
    pass

def print_all(fns):
    for fn in fns:

        print(f"{fn.__name__}: ", end='')
        nodes_checked = []
        fn(graph, goal_test_producer(nodes_checked))
        print('-'.join(nodes_checked))

print_all([dfs_tree, dfs_graph, bfs_tree, bfs_graph])

# Now implement with early goal test to see the difference
def dfs_early_tree(graph, goal_test, start='S'):
    # TODO Implement this
    frontier = [start]
    while frontier:
        node = frontier.pop()
        if goal_test(node):
            return node
        if("G" in graph[node]):
            goal_test("G")
            return "G"
        frontier.extend(sorted(graph[node]))
    return None
    pass

def dfs_early_graph(graph, goal_test, start='S'):
    # TODO Implement this
    explored, frontier = set(), [start]
    while frontier:
        node = frontier.pop()
        if goal_test(node):
            return node
        if("G" in graph[node]):
            goal_test("G")
            return "G"
        explored.add(node)
        frontier.extend(sorted(graph[node] - explored - set(frontier)))
    return None

def bfs_early_tree(graph, goal_test, start='S'):
    # TODO Implement this
    frontier = [start]
    while frontier:
        node = frontier.pop(0)
        if goal_test(node):
            return node
        # add each children into the frontier
        if("G" in graph[node]):
            goal_test("G")
            return "G"
        for x in sorted(graph[node]):
            # print(x, end="->")
            frontier.extend(x)
    return None     

def bfs_early_graph(graph, goal_test, start='S'):
    # TODO Implement this
    explored, frontier = set(), [start]
    while frontier:
        node = frontier.pop(0)
        if goal_test(node):
            return node
        # add each children into the frontier
        if("G" in graph[node]):
            goal_test("G")
            return "G"
        for x in sorted(graph[node]):
            if(x not in explored):
                explored.add(x)
                frontier.extend(x)
            

print_all([dfs_early_tree, dfs_early_graph, bfs_early_tree, bfs_early_graph])