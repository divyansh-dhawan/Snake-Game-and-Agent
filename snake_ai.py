# snake_ai.py

import heapq

GRID_SIZE = 20
WIDTH = 600
HEIGHT = 600
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

def position_to_grid(pos):
    return (int((pos[0] + WIDTH // 2) // GRID_SIZE), int((pos[1] + HEIGHT // 2) // GRID_SIZE))

def grid_to_position(grid):
    return (grid[0] * GRID_SIZE - WIDTH // 2 + 10, grid[1] * GRID_SIZE - HEIGHT // 2 + 10)

def get_neighbors(node):
    x, y = node
    return [(x + dx, y + dy) for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]
            if 0 <= x + dx < GRID_WIDTH and 0 <= y + dy < GRID_HEIGHT]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def a_star(start, goal, obstacles):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for neighbor in get_neighbors(current):
            if neighbor in obstacles:
                continue
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []
