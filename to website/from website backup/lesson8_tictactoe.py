def main():
    grid = [[0,0,0],[0,0,0],[0,0,0]] # Empty 3x3 list
    playerNow = 'X'

    while IsEndPosition(grid) == False:
        row, col = int(input('Row: ')), int(input('Col: '))
        if not Grid_InRange(row,col):
            print(f'The position ({row},{col}) is not in range!')
        elif not Grid_IsEmpty(row,col,grid):
            print(f'The position ({row},{col}) is occupied!')
        else:
            grid[row][col] = playerNow
            playerNow = GetNextPlayer(playerNow)
            Print_Grid(grid)

    winner = IsEndPosition(grid)
    if winner == 'Tie':
        print('Tie!')
    else:
        print(f'{winner} is the winner')
    input()

def IsEndPosition(grid):
    
    for i in range(3):
        # Check all rows 
        if grid[i][0] == grid[i][1] and grid[i][0] == grid[i][2] and grid[i][0] != 0:
            return grid[i][0]
        # Check all columns
        if grid[0][i] == grid[1][i] and grid[0][i] == grid[2][i] and  grid[0][i] != 0:
            return grid[0][i]

    # Check Diagonals
    if grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2] and grid[1][1] != 0:
        return grid[1][1]
    if grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0] and grid[1][1] != 0:
        return grid[1][1]
    
    # Check if all cells filled
    isFull = True
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                isFull = False
                break
    if isFull:
        return 'Tie'
    return False

def Print_Grid(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] != 0:
                print(grid[i][j],end='')
            else:
                print('-',end='')
        print('')

def Grid_IsEmpty(row,col,grid):
    return grid[row][col] == 0

def Grid_InRange(row,col):
    return 0<=row and row <=2 and 0 <= col and col <= 2

def GetNextPlayer(playerNow):
    if playerNow == 'X':
        return 'O'
    else:
        return 'X'

if __name__ == "__main__":
    main()

