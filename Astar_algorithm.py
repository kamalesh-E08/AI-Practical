import heapq
class State:
    def __init_(self, x, y, cost):
        self.x = x
        self.y = y  
        self.cost=cost

    def __lt__(self, other):
        return self.cost < other.cost

def get_neighbors(current_node):

    x, y = current_node.x, current_node.y

    neighbors = [(x - 1, y), (x + 1, y),(x, y - 1),(x, y + 1), (x - 1, y - 1),(x - 1, y + 1),(x + 1, y - 1),(x + 1, y + 1),]
    valid_neighbors =[]
    for neighbor_x, neighbor_y in neighbors:
        if ( 0<=neighbor_x < len (grid) and 0<=neighbor_y < len(grid[0]) and grid[neighbor_x][neighbor_y] == 0 ):
            valid_neighbors.append(State(neighbor_x, neighbor_y, current_node.cost + 1))
    return valid_neighbors

def heuristic(node):
    return abs(node.x-goal[0]) + abs(node.y-goal[1])

def astar_search(grid, start, goal):
    open_list=[]
    closed_set=set()
    start_node=State(start[0], start[1], 0)
    heapq.heappush(open_list, (start_node.cost+heuristic(start_node), start_node))
    while open_list: 
        current_node=heapq.heappop(open_list)[1]
        if (current_node.x, current_node.y) == goal:
            return current_node.cost
        if (current_node.x, current_node.y) in closed_set:
            continue

        closed_set.add((current_node.x, current_node.y))
        neighbors= get_neighbors(current_node)
        for neighbor_node in neighbors: 
            heapq.heappush(open_list, (neighbor_node.cost + heuristic(neighbor_node), neighbor_node))

    return float("inf")

if __name__=="__main__":
    grid=[
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
        ]
    start = (0, 0)
    goal = (4, 4)
    shortest_path_length = astar_search(grid, start, goal)
    print(f"Shortest path length: {shortest_path_length}")