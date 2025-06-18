from random import randint


grid = [["~","~","~","~","~","~","~","~","~","~",],
        ["~","~","~","~","~","~","~","~","#","~",],
        ["~","#","~","#","#","#","#","#","~","~",],
        ["~","#","~","~","~","~","~","~","~","~",],
        ["~","#","~","#","#","#","#","~","~","~",],
        ["~","~","~","~","~","~","~","~","~","~",],
        ["~","~","~","#","~","~","~","#","#","~",],
        ["~","~","~","#","~","~","~","~","~","~",],
        ["~","~","~","#","~","~","~","~","~","~",],
        ["~","~","~","~","~","~","~","~","~","~",],]
schiff_getroffen = "X"
wasser_getroffen = "O"
wasser = "~"
schiff = "#"


def render_grid(l_grid):
    for row in l_grid:
        for field in row:
            print(field,end="")
        print()
def shoot_on_board(l_grid):
    x = randint(0,9)
    y = randint(0,9)
    return x,y

def check_end_game(l_grid : list[list[str]]):
    for row in l_grid:
        for field in row:
            if field == schiff:
                return False
    return True

render_grid(grid)


def double_hit(l_grid):
    treffer = True

    while treffer:    
        x,y = shoot_on_board(l_grid)
        if grid [x][y] == schiff_getroffen or wasser_getroffen:
            treffer = True
        else:
            treffer = False
            return x,y    
    
    



while check_end_game(grid):
    x,y = shoot_on_board(grid)
    if grid[y][x] == schiff:
        grid[y][x] = schiff_getroffen
    if grid[y][x] == wasser:
        grid[y][x] = wasser_getroffen
    # Clear cmd
    print("\033[H\033[J", end="")
    render_grid(grid)
    input()