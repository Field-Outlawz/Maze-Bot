import numpy as np
import matplotlib.pyplot as plt

# Define the maze structure
maze = np.array([
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,0,0,0,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,1,1,1,1,1],
    [1,3,1,1,1,1,0,0,0,1,1,1,1],
    [1,1,1,0,1,1,1,1,0,1,1,1,1],
])

# Define the possible movements (up, down, left, right)
movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Function to explore the maze and find the shortest path
def explore_maze(maze, start):
    path = []
    current = start
    visited = set()  # Track visited positions to avoid cycles

    while maze[current[0], current[1]] != 3:
        maze[current[0], current[1]] = 4
        visited.add((current[0], current[1]))  # Mark current position as visited

        for movement in movements:
            new_position = (current[0] + movement[0], current[1] + movement[1])

            if (0 <= new_position[0] < maze.shape[0] and 
                0 <= new_position[1] < maze.shape[1] and
                maze[new_position[0], new_position[1]] != 4 and
                new_position not in visited):  # Check if not visited

                if maze[new_position[0], new_position[1]] == 3:
                    path.append(new_position)
                    return path

                if maze[new_position[0], new_position[1]] != 1:
                    path.append(new_position)
                    current = new_position
                    break

        else:  # Backtrack if no suitable neighbor found
            if path:  # Only backtrack if the path is not empty
                path.pop()
                current = path[-1]
            else:  # If path is empty, no path found
                return None

    return path

# Find the starting point
start = np.argwhere(maze == 2)[0]

# Explore the maze and find the shortest path
path = explore_maze(maze, start)

# Visualize the maze and path
plt.imshow(maze, cmap='binary')
plt.plot([start[1]], [start[0]], 'go')  # Starting point
if path is not None:
    plt.plot([point[1] for point in path], [point[0] for point in path], 'r-')  # Path
    plt.plot([path[-1][1]], [path[-1][0]], 'ro')  # Ending point
plt.show()
print("THank You")
