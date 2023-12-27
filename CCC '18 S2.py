N = int(input())

grid = [[int(i) for i in input().split()] for _ in range(N)]

def rotate(grid):
    return [list(reversed(col)) for col in zip(*grid)]

while True:
    col1 = [grid[i][0] for i in range(len(grid))]
    if grid[0] == sorted(grid[0]) and col1 == sorted(col1):
        for i in grid:
            print(*i)
        break
    
    else:
        grid = rotate(grid)
