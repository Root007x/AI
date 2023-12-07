from collections import deque

def bfs(graph,src,goal):
    if(src == goal):
        return True

    frontier = deque() # queue
    frontier.append(src)
    explored = []

    while frontier:
        node = frontier.popleft()
        explored.append(node)

        for it in graph[node]:
            child = it;
            if child not in explored and child not in frontier:
                if(child == goal):
                    return True
                frontier.append(child)
    return False


if __name__ == "__main__":
    graph = {
        'S' : ['A','B'], # key : value
        'A' : ['C','D'],
        'B' : ['E','F'],
        'C' : ['G','H'],
        'D' : [],
        'E' : ['I'],
        'F' : [],
        'G' : ['J'],
        'H' : [],
        'I' : [],
        'J' : []
    }

    src = 'S'
    goal = 'J'

    if bfs(graph,src,goal):
        print("Found Goal")
    else:
        print("Not Found")





