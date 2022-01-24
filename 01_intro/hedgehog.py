#!/usr/bin/env python3

"""
10 hedgehogs glued to each other. It can be seen as a U shape form, of two rows (two U forms glued to each other)

Front side:

H0    H4
H1 H2 H3


Back side:

H5    H9
H6 H7 H8


9
W W W W W W W W W
W 6 7 8 - - - - W
W 1 2 3 - - - - W
W - - - - - - - W
W - - - - - - - B F F
W - - - - - - - B F F
W - - - - - - - W
W - - - - - - - W
W W W W W W W W W

"""

import sys

input_buf="""
W W W W W W W W W
W - - - B - - - W
W - - - - - - - W
W - - B - - - - W
W - - - B - - - B F F
W - - - - 0 1 - B F F
W - - - - - 2 - W
W - - B - 4 3 - W
W W W W W W W W W
"""

# "W" - wall
# "-" - free
# "B" - blockage
# "F" - finish

WALL=0
FREE=1
BLOCK=2
FINISH=3

NORTH=0
SOUTH=1
WEST=2
EAST=3

debug_directions = {WEST:"V",EAST:"E",SOUTH:"S",NORTH:"N"}


rotate_around=[ [0,5], [4,9], [2,2], [0,1], # if rotate around 0 and 5 we get 4,9 touching at +2, +2 in the direction of rotation, having unmodified coordinates relative to first point (0)
                [4,9], [3,8], [1,1], [0,1],
                [3,8], [2,1,7,6], [1,2,1,2], [0,0,1,1],
                [1,6], [0,5], [1,1], [0,1], # back to 0,5
                
                [5,0], [6,1], [1,1], [0,1],
                [6,1], [7,8,2,3], [1,2,1,2], [0,0,1,1],
                [8,3], [9,4], [1,1],[0,1],
                [9,4], [5,0], [2,2],[0,1], # back to 5,0
                
                [6,5], [1,0], [1,1],[0,1],
                [1,0], [2,3,4], [1,2,2],[0,0,1],
                [3,4], [8,9], [1,1],[0,1],
                [8,9], [5,6,7], [2,2,1], [1,0,0], # back to 6,5
                
                [0,1], [5,6], [1,1],[0,1],
                [5,6], [7,8,9], [1,2,2],[1,1,0],
                [9,8], [4,3], [1,1],[0,1],
                [4,3], [2,1,0], [1,2,2], [1,1,0],# back to 0,1
                
                [1,2,3], [6,7,8], [1,1,1], [0,1,2],
                [6,7,8], [5,9], [1,1], [0,2],
                [5,9], [0,4], [1,1], [0,2],
                [0,4], [1,2,3], [1,1,1],[0,1,2], # back to [1,2,3]

                [3,2,1], [4,0], [1,1],[0,2],
                [4,0], [9,5], [1,1],[0,2],
                [9,5], [8,7,6], [1,1,1],[0,1,2],
                [8,7,6], [3,2,1], [1,1,1],[0,1,2],

              ]

def find_rotation_index(arr):
    sz = len(rotate_around)
    assert(sz % 4 == 0)
    i=0
    while i < sz:
        if rotate_around[i] == arr:
            return i
        i+=4
    print("Not found:" + str(arr))
    return -1
    
def get_move(hhs,direction):
    if hhs is None:
        return None
        
    if len(hhs) < 4: # minimum 4 points "touching" the maze
        return None
    
    new_hhs = {}
        
    if direction == NORTH or direction == SOUTH:
        # find top points
        should_reverse= (direction == SOUTH)
        sign= -1 if should_reverse else 1
        min_max = min if direction == NORTH else max
        
        
        yrot = min_max( v[0] for v in hhs.values() ) # these will be kept
        points = [ p for p in hhs.keys() if hhs[p][0] == yrot ]
        points.sort(key = lambda p : hhs[p][1], reverse=should_reverse)
        index = find_rotation_index(points)
        assert(index > -1)
        
        for p in points:
            new_hhs[p] = hhs[p]
            
        new_points = rotate_around[index+1]
        new_y = [ yrot - sign*diff for diff in rotate_around[index+2] ]
        offset0 = rotate_around[index+3]
        assert( len(new_points) == len(new_y) )
        assert( len(offset0) == len(new_y) )
        
        for i in range(len(new_y)):
            new_hhs[new_points[i]] = [ new_y[i], hhs[points[0]][1] + sign*offset0[i] ]
        
        return new_hhs
        
    # if direction == SOUTH:
        # should_reverse=True
        # sign=-1
        # # find bottom points
        # maxy = max( v[0] for v in hhs.values() ) # these will be kept
        # # print(maxy)
        # points = [ p for p in hhs.keys() if hhs[p][0] == maxy ]
        # # sort points in X order
        # points.sort(key = lambda p : hhs[p][1], reverse=should_reverse )
        # index = find_rotation_index(points)
        # assert(index > -1)
        
        # for p in points:
            # new_hhs[p] = hhs[p]
        
        # new_points = rotate_around[index+1]
        # new_y = [ maxy + diff for diff in rotate_around[index+2] ]
        # offset0 = rotate_around[index+3]
        # assert( len(new_points) == len(new_y) )
        # assert( len(offset0) == len(new_y) )
        
        # # print(offset0)
        
        # for i in range(len(new_y)):
            # new_hhs[new_points[i]] = [ new_y[i], hhs[points[0]][1] + sign*offset0[i] ]
        
        # return new_hhs
        
    elif direction == EAST or direction == WEST:
        # find right/left points
        should_reverse= (direction == WEST)
        sign=-1 if should_reverse else 1
        min_max = min if direction == WEST else max
        
        xrot = min_max( v[1] for v in hhs.values() ) # these will be kept
        points = [ p for p in hhs.keys() if hhs[p][1] == xrot ]
        #print(points)
        points.sort(key = lambda p : hhs[p][0], reverse=should_reverse)
        index = find_rotation_index(points)
        assert(index > -1)
        
        for p in points:
            new_hhs[p] = hhs[p]
        
        new_points = rotate_around[index+1]
        #print(new_points)
        new_x = [ xrot + sign*diff for diff in rotate_around[index+2] ]
        #print(new_x)
        offset0 = rotate_around[index+3]
        #print(offset0)
        assert( len(new_points) == len(new_x) )
        assert( len(offset0) == len(new_x) )
        
        for i in range(len(new_x)):
            new_hhs[new_points[i]] = [ hhs[points[0]][0] + sign*offset0[i], new_x[i] ]
        
        return new_hhs

    else:
        raise Exception("Unknown direction:"+str(direction))

HEDGE_HOGS = [ str(i) for i in range(10) ]

def get_hh_index(hhs,x,y):
    #print(hhs)
    #print([y,x])
    for k,v in hhs.items():
        if v == [y,x]:
            return k
    return None

def display_maze(maze, hhs):
    y=0
    for ml in maze:
        s = ''
        x=0
        for b in ml:
            ch = None
            if b == WALL:
                ch = 'W'
            elif b == BLOCK:
                ch = 'B'
            elif b == FREE:
                ch = '-'
            elif b == FINISH:
                ch = 'F'
            else:
                raise Exception("Unexpected maze block:"+str(b))
            hhi = get_hh_index(hhs,x,y)
            s+=' '
            if hhi is not None:
                ch = str(hhi)
            s+=ch
            x+=1
        print(s)
        y+=1

def is_at_the_end(maze,hhs):
    for k in hhs:
        v = hhs[k]
        y = v[0]
        x = v[1]
        if maze[y][x] != FINISH:
            return False
    
    return True

def is_ok(maze,hhs):
    for k,v in hhs.items():
        y = v[0]
        x = v[1]
        if y >= len(maze) or y < 0:
            return False
        line = maze[y]
        if x >= len(line) or x < 0:
            return False
        if line[x] != FREE and line[x] != FINISH:
            return False
    
    return True

def wait(text):
    #print(text)
    #input(text)
    pass

been_there=[]
depth=0

def find_exit(maze,hhs):
    global been_there
    global depth
    if hhs in been_there:
        wait("already passed here")
        return None

    depth+=1
    #display_maze(maze,hhs)
    wait('start ' + str(depth))

    been_there.append(hhs)
    ret_result = None
    for dir in [ NORTH, SOUTH, EAST, WEST ]:
        new_hhs = get_move(hhs, dir)
        if not is_ok(maze,new_hhs):
            #display_maze(maze,new_hhs)
            wait('move not ok '+debug_directions[dir])
            continue
            
        #display_maze(maze,new_hhs)
        wait('newpos from ' + debug_directions[dir])
        if is_at_the_end(maze,new_hhs):
            wait('is at the end !')
            ret_result = [ dir ]
            break
        
        path = find_exit(maze,new_hhs)
        if path is None:
            wait('No path found')
            continue
        
        if len(path) > 0:
            ret_result = [dir] + path
            break
    
    depth-=1
    return ret_result

def get_path(maze,hhs):
    if is_at_the_end(maze,hhs):
        return [] # already at the end
    return find_exit(maze,hhs)

def display_result(res):
    if res is None:
        print('No result.')
        return
    
    count = -1
    ret = ''
    for r in res:
        count+=1
        if count == 4:
            count = 0
            ret += ' '
        ret += debug_directions[r]
    
    print(ret)

maze = []
start_hhs={}

for line in input_buf.split('\n'):
    line = line.strip()
    if len(line)==0:
        continue
    parts = line.split(' ')
    maze_line = []
    
    line_index = len(maze)
    for part in parts:
        part = part.strip()
        if len(part) == 0:
            continue
        
        if part == "W":
            maze_line.append(WALL)
        elif part == "-":
            maze_line.append(FREE)
        elif part == "B":
            maze_line.append(BLOCK)
        elif part == "F":
            maze_line.append(FINISH)
        elif part in HEDGE_HOGS:
            int_val = int(part)
            column_index = len(maze_line)
            start_hhs[int_val] = [line_index, column_index]
            maze_line.append(FREE)
        else:
            raise Exception("Unexpected value:" + part);
    
    maze.append(maze_line)

result = get_path(maze,start_hhs)

display_result(result)
