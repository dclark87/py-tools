def findCoordDict(maze, rows, columns):
    coord_dict = {}
    for i in xrange(rows):
        for j in xrange(columns):
            paths = []
            if maze[i][j] == 1:
                continue
            if i < rows - 1:
                up = (i + 1, j)
                if maze[i+1][j] == 0:
                    paths.append(up)
            # Down
            if i > 0:
                down = (i - 1, j)
                if maze[i-1][j] == 0:
                    paths.append(down)
            # Left
            if j > 0:
                left = (i, j - 1)
                if maze[i][j-1] == 0:
                    paths.append(left)
            # Right
            if j < columns - 1:
                right = (i, j + 1)
                if maze[i][j+1] == 0:
                    paths.append(right)
            coord_dict[(i, j)] = paths

    # return
    return coord_dict


def bfsCoords(maze, rows, columns, exitRow, exitCol):
    # Start at entrance
    import collections
    coord_dict = findCoordDict(maze, rows, columns)
    queue = collections.deque()
    queue.append(((0, 0), []))
    exit = (exitRow, exitCol)

    # Breadth-first search
    while len(queue) > 0:
        # Get current position
        coord, path = queue.popleft()

        for nbr in coord_dict[coord]:
            if nbr in path:
                continue
            if nbr == exit:
                yield path + [nbr]
            else:
                queue.append((nbr, path + [nbr]))


def findMinNumSteps(maze, rows, columns, exitRow, exitCol):
    '''
    Function to find the minimum steps from entrance of maze to exit
    '''

    import sys

    shortest = sys.maxint
    for path in bfsCoords(maze, rows, columns, exitRow, exitCol):
        if len(path) < shortest:
            shortest = len(path)
    if shortest == sys.maxint:
        return -1

    return shortest


print(findMinNumSteps([[0, 0, 0, 0],
                       [1, 0, 1, 0],
                       [1, 0, 0, 0]],
                      3, 4, 1, 1))