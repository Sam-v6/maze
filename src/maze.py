from pyamaze import maze,COLOR,agent
import random

# Create maze
ROWS = 10
COLUMNS = 10
m=maze(ROWS, COLUMNS)
m.CreateMaze()
particpant=agent(m,shape='square',footprints=True)

# Init
current_row = ROWS
current_col = COLUMNS
open_directions = []
move_count = 0
solved_maze = False

# Set path
while move_count < 10e3 and solved_maze == False:

    # Init
    open_directions.clear()

    # Get the East, West, North, and South info
    direction_info = m.maze_map[(current_row,current_col)]

    # Create a list of the open directions
    for key in direction_info:
        if direction_info[key] == 1:
            open_directions.append(key)

    # Select a random open direction
    selected_direction_index = random.randint(0,len(open_directions)-1)
    selected_direction = open_directions[selected_direction_index]

    # Translate selection direction into row & column commands
    if selected_direction == 'E':
        current_col = current_col+1
    elif selected_direction == 'W':
        current_col = current_col-1
    elif selected_direction == 'N':
        current_row = current_row-1
    elif selected_direction == 'S':
        current_row = current_row+1
    else:
        print("ERROR, no open direction")

    # Command position chage
    particpant.position=(current_row,current_col)

    # Update move count and success criteria
    move_count = move_count + 1
    if current_row == 1 and current_col == 1:
        solved_maze = True

    # Status
    print("Move Count:", move_count)
    print("Selected Direction:", selected_direction)
    print("New Position:", current_row, current_col)

# Run maze
m.run()