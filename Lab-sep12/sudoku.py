r1 = 999
c1 = 999
def solveSudoku(grid, n):
    global r1
    global c1
    if not findUnallocated(grid, n):
        return True
    for num in range(1, n+1):
        if isSafe(grid, r1, c1, num):
            grid[r1][c1] = num
            if solveSudoku(grid, n):
                return True
            grid[r1][c1] = 0
    return False

def findUnallocated(grid, n):
    global r1
    global c1
    for i in range(n):
        r1 =i
        for j in range(n):
            c1 = j
            if grid[i][j] == 0:
                return True
    return False


def isSafe(grid, row, col, num):
    global sqn
    return not usedInRow(grid, row, num) and not usedInCol(grid, col, num) and not usedInSub(grid, row - row%sqn, col - col%sqn, num)


def usedInRow(grid, row, num):
    global n
    for c in range(n):
        if grid[row][c] == num:
            return True
    return False


def usedInCol(grid, col, num):
    global n
    for r in range(n):
        if grid[r][col] == num:
            return True
    return False

def usedInSub(grid, r, c, num):
    global sqn
    for row in range(sqn):
        for col in range(sqn):
            if grid[row + r][col + c] == num:
                return True
    return False


grid = []
n = 4
sqn = 2
print(f'Enter {n}X{n} grid')
for _ in range(n):
    l = list(map(int, input().split()))
    grid.append(l)

print()
flag = solveSudoku(grid, n)
if flag:
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=' ')
        print()
else:
    print("No solution ")


'''
OUTPUT

Enter 4X4 grid
0 0 3 4
3 4 0 0
0 0 4 3
0 3 2 0

1 2 3 4 
3 4 1 2 
2 1 4 3 
4 3 2 1 
'''