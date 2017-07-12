# Complete the function below.
class Graph(object):
    def __init__(self):
        self.nodes = {}


class Node(object):
    def __init__(self, val):
        self.val = val
        self.nbrs = {}


def build_graph(friends):
    graph = Graph()
    for i, stu in enumerate(friends):
        if i in graph.nodes:
            node = graph.nodes[i]
        else:
            node = Node(i)

        for j, frd in enumerate(stu):
            if j != i and frd == 'Y':
                if j in graph.nodes:
                    fnode = graph.nodes[j]
                else:
                    fnode = Node(j)
                    graph.nodes[j] = fnode
                if j not in node.nbrs:
                    node.nbrs[j] = fnode
            graph.nodes[i] = node

    return graph


def friend_circles(friends):
    graph = build_graph(friends)

    nodes = graph.nodes.keys()
    stack = []
    visited = set()
    circles = []
    path = []
    while nodes:
        val = nodes.pop()
        if val in visited:
            continue
        visited.add(val)
        stack.append(graph.nodes[val])
        path.append(val)
        while stack:
            node = stack.pop()
            for val, nbr in node.nbrs.items():
                if val not in visited:
                    stack.append(nbr)
                    visited.add(val)
                    path.append(val)
        circles.append(path)
        path = []

    return len(circles)


if __name__ == '__main__':
    friends = [['Y', 'Y', 'N', 'N'],
               ['Y', 'Y', 'Y', 'N'],
               ['N', 'Y', 'Y', 'N'],
               ['N', 'N', 'N', 'Y']]
    print(friend_circles(friends))