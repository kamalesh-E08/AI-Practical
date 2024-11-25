from queue import PriorityQueue
class TwoByTwoPuzzle:
    def __init__ (self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def is_goal(self, state): 
        return state == self.goal_state

    def heuristic(self, state): 
        return sum(1 for i in range(2) for j in range(2) if state[i][j] != self.goal_state[i][j])
    
    def get_neighbors(self, state):
        empty_tile=(0, 0)
        moves = [(0, 1), (1, 0), (-1,0), (0,-1)] 
        neighbors = []
        for move in moves:
            new_x, new_y = empty_tile[0] + move[0], empty_tile[1] + move[1] 
            if 0 <= new_x<2 and 0 <= new_y <2:

                new_state = [list(row) for row in state] 
                new_state[empty_tile[0]][empty_tile[1]], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_tile[0]][empty_tile[1]] 
                neighbors.append(new_state)
        return neighbors

    def solve(self): 
        frontier = PriorityQueue() 
        frontier.put((self.heuristic(self.initial_state), self.initial_state)) 
        came_from = {} 
        cost_so_far = {self.initial_state: 0}

        while not frontier.empty(): 
            current_state=frontier.get()[1]
            if self.is_goal(current_state):
                path = [current_state] 
                while current_state != self.initial_state: 
                    current_state = came_from[current_state] 
                    path.append(current_state) 
                path.reverse() 
                return path
            for neighbor_state in self.get_neighbors(current_state) :   
                new_cost = cost_so_far[current_state] + 1 
                if neighbor_state not in cost_so_far or new_cost < cost_so_far[neighbor_state]: 
                    cost_so_far[neighbor_state]=new_cost 
                    priority=new_cost + self.heuristic(neighbor_state) 
                    frontier.put((priority, neighbor_state)) 
                    came_from[neighbor_state]=current_state
        return None

initial_state_2x2=[[2, 1],[0,3]]
goal_state_2x2 = [[1,2],[3,0]]
puzzle_2x2 = TwoByTwoPuzzle(initial_state_2x2, goal_state_2x2) 
solution_2x2 = puzzle_2x2.solve()

if solution_2x2:
    for step, state in enumerate(solution_2x2): 
        print(f"Step {step + 1}:")
    for row in state:
        print(row)
    print()
else:
    print("No solution found.")