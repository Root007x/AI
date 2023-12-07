from collections import deque

def dfs(graph,src,goal):
    if(src == goal):
        return True

    stack = deque()
    stack.append(src)
    explored = []

    while stack:
        node = stack.pop()
        explored.append(node)

        for it in graph[node]:
            child = it;
            if child not in explored and child not in stack:
                if(child == goal):
                    return True
            stack.append(child)
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

    if dfs(graph,src,goal):
        print("Found Goal")
    else:
        print("Not Found")
