from collections import deque


def baby_shark(N, grid):
    # Directions: up, left, right, down
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    # Find initial position of baby shark
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 9:
                shark_x, shark_y = i, j
                grid[i][j] = 0  # Empty the starting position
                break

    shark_size = 2  # Initial size
    eaten = 0  # Number of fish eaten
    time = 0  # Total time elapsed

    while True:
        # BFS to find the nearest prey
        visited = [[-1] * N for _ in range(N)]
        queue = deque()
        queue.append((shark_x, shark_y))
        visited[shark_x][shark_y] = 0
        candidates = []
        min_dist = None

        while queue:
            x, y = queue.popleft()
            dist = visited[x][y]

            # If we have found a fish and current distance exceeds min_dist, we can stop
            if min_dist is not None and dist > min_dist:
                break

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                    can_move = grid[nx][ny] <= shark_size
                    if can_move:
                        visited[nx][ny] = dist + 1
                        queue.append((nx, ny))
                        # If there is a fish smaller than shark's size, it's a candidate
                        if 0 < grid[nx][ny] < shark_size:
                            if min_dist is None or dist + 1 <= min_dist:
                                min_dist = dist + 1
                                candidates.append((dist + 1, nx, ny))
        # No candidates found
        if not candidates:
            break

        # Sort candidates to select the one according to the rules
        candidates.sort()
        dist, fish_x, fish_y = candidates[0]

        # Eat the fish
        time += dist
        eaten += 1
        grid[fish_x][fish_y] = 0  # Remove the fish from the grid

        # Update shark's position
        shark_x, shark_y = fish_x, fish_y

        # Check if shark grows
        if eaten == shark_size:
            shark_size += 1
            eaten = 0

    return time


# Read input
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# Run the simulation and print the result
print(baby_shark(N, grid))
