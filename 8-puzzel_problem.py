import random
goal_state = [[1, 2, 3] , [4, 5, 6], [7, 8, 0] ]

def generate_initial_state(): 
    initial_state = goal_state[:] 
    for _ in range(100): # Shuffle the initial state
        neighbors = get_neighbors(initial_state) 
        initial_state = random.choice(neighbors) 
    return initial_state

def misplaced_tiles(state):
    count = 0 
    for i in range(3):
        for j in range(3): 
            if state[i][j] != goal_state[i][j]:
                count += 1
    return count

def get_neighbors(state):
    neighbors =[] 
    for i in range(3): 
        for j in range(3): 
            if state[i][j] == 0 :
                if i > 0:
                    neighbor= [row[:] for row in state] 
                    neighbor[i][j], neighbor[i-1][j] = neighbor[i - 1][j], neighbor[i][j]
                    neighbors.append(neighbor) 
                if i < 2:
                    neighbor = [row[:] for row in state] 
                    neighbor[i][j], neighbor[i+1][j] = neighbor[i+1][j], neighbor[i][j]
                    neighbors.append(neighbor)
                if j>0:
                    neighbor = [row[:] for row in state]
                    neighbor[i][j], neighbor[i][j-1] = neighbor[i][j-1], neighbor[i][j]
                    neighbors.append(neighbor)
                if j <2:
                    neighbor = [row[:] for row in state]
                    neighbor[i][j], neighbor[i][j+1] = neighbor[i][j + 1], neighbor[i][j]
                    neighbors.append(neighbor)
    return neighbors

def hill_climbing(initial_state):
    current_state=initial_state
    while True: 
        neighbors = get_neighbors(current_state) 
        best_neighbor = min(neighbors, key=misplaced_tiles) 
        if misplaced_tiles(best_neighbor) >= misplaced_tiles(current_state): 
            return current_state 
        current_state = best_neighbor

def print_puzzle(state):

    for row in state:
        print(row) 
    print()

initial_state = generate_initial_state()
print("Initial State:")
print_puzzle(initial_state)
final_state = hill_climbing(initial_state)
print("Final State (Solved):")
print_puzzle(final_state)