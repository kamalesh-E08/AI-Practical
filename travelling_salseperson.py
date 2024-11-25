import numpy as np

def nearest_neighbor_tsp(dist_matrix):
    num_cities= len(dist_matrix)
    visited =[False]*num_cities
    tour = []
    total_distance = 0
    current_city=0
    for _ in range(num_cities - 1):
        visited[current_city] = True
        tour.append(current_city)
        nearest_city= None
        min_distance=float('inf')
    for city in range(num_cities):
        if not visited[city] and dist_matrix[current_city][city] <min_distance:
            nearest_city = city
            min_distance=dist_matrix[current_city][city]
    total_distance += min_distance
    current_city = nearest_city
    tour.append(tour[0])
    total_distance + dist_matrix[current_city][tour[0]]
    return tour, total_distance

dist_matrix = np.array([[0, 29, 20, 21],
[29, 0, 15, 17],
[20, 15, 0, 28],
[21, 17, 28, 0]])
tour, total_distance = nearest_neighbor_tsp(dist_matrix)
print("Tour Order:", tour)

print("Total Distance:", total_distance)