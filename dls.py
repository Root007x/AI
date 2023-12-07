def depth_limited_search(graph,src,goal,limit):
    return recursive_dls(graph,src,goal,limit)

def recursive_dls(graph,src,goal,limit):
    if src == goal:
        return "Goal Found"
    elif limit == 0: # base case
        return "Cutoff" # cutoff means in the given limit there is no goal
    else:
        cutoff_occured = False

        for it in graph[src]:
            child = it
            result = recursive_dls(graph,child,goal,limit - 1) # recursive call

            if result == "Cutoff":
                cutoff_occured = True
            elif result != "Failure":
                return result
            
        if cutoff_occured:
            return "Cutoff"
        else:
            return "Failure"


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
    limit = 2

    print(depth_limited_search(graph,src,goal,limit))