import copy, random, sys, time

WIDTH = 40
HEIGHT = 5

ALIVE = 'o'
DEAD = ' '

next_cells = {}

for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            next_cells[(x, y)] = ALIVE
        else:
            next_cells[(x, y)] = DEAD

while True:
    print('\n' * 50)
    cells = copy.deepcopy(next_cells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')
        print()
    print('Press Ctrl-c to quit')

    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            top = (y - 1) % HEIGHT
            bottom = (y + 1) % HEIGHT

            alive_neighbors_count = 0

            if cells[(left, top)] == ALIVE:
                alive_neighbors_count += 1
            if cells[(x, top)] == ALIVE:
                alive_neighbors_count += 1
            if cells[(right, top)] == ALIVE:
                alive_neighbors_count += 1
            if cells[(x, bottom)] == ALIVE:
                alive_neighbors_count += 1
            if cells[(right, y)] == ALIVE:
                alive_neighbors_count += 1
            if cells[(left, y)] == ALIVE:
                alive_neighbors_count += 1
            if cells[(left, bottom)] == ALIVE:
                alive_neighbors_count += 1
            if cells[(right, bottom)] == ALIVE:
                alive_neighbors_count += 1
                
            if cells[(x, y)] == ALIVE and (alive_neighbors_count == 2 or alive_neighbors_count == 3):
                next_cells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and alive_neighbors_count == 3:
                next_cells[(x, y)] = ALIVE
            else:
                next_cells[(x, y)] = DEAD

    try:
        time.sleep(0.5)
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        sys.exit() 
            
