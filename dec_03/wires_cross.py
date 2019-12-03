import os
import numpy as np
from matplotlib import pyplot

path = os.path.dirname(os.path.abspath(__file__))
# print(path)
f = open(os.path.join(path,'wires_paths1.txt'), 'r')
wire_paths = f.read()

[red_wire_path, blue_wire_path] = wire_paths.split('\n')

# print('Red wire path:\n', red_wire_path)
# print('Blue wire path:\n', blue_wire_path)

def get_wire_moves_list(wire_string):
    wire_string.replace(' ','')
    l = wire_string.split(',')
    dirs = [k[0] for k in l]
    distances = [int(k[1:]) for k in l]
    return dirs, distances

dirs_red, dist_red = get_wire_moves_list(red_wire_path)
dirs_blue, dist_blue = get_wire_moves_list(blue_wire_path)
# print('Red wire:\n')
# print(dirs_red)
# print(dist_red)
# print(max(dist_red))
# print('Blue wire:\n')
# print(dirs_blue)
# print(dist_blue)
# print(max(dist_blue))

def get_max_dimensions(dirs, dist):
    max_x=0
    max_y=0
    x=0
    y=0
    index=0
    for d in dirs:
        if d in ['L', 'R']:
            if d=='L':
                x-=dist[index]
            else:
                x+=dist[index]
            if abs(x)>max_x:
                max_x=abs(x)
            # print('Max_x ',str(max_x))
        if d in ['U','D']:
            if d=='U':
                y+=dist[index]
            else:
                y-=dist[index]
            if abs(y)>max_y:
                max_y=abs(y)
            # print('Max_y ',str(max_y))
        index+=1
    return max_x, max_y
        
max_x_red, max_y_red = get_max_dimensions(dirs_red, dist_red)
max_x_blue, max_y_blue = get_max_dimensions(dirs_blue, dist_blue)

# print(max_x_red, max_x_blue)
# print(max_y_red, max_y_blue)

max_x = max(max_x_red, max_x_blue)
max_y = max(max_y_red, max_y_blue)
        
print(max_x, max_y)
        
wires_map = np.zeros((max_x, max_y), dtype=int)

def trace_wire_path(map, dirs, dist, x_origin=0, y_origin=0):
    index = 0
    x=x_origin
    y=y_origin
    map[x,y]=1
    for d in dist:
        dir = dirs[index]
        print('Dir ', dir)
        index+=1
        if dir=='R':
            # print('x0',str(x))
            # print('dist',str(d))
            process_row_move(map,x,x+d,y)
            x=x+d
            # print('x1',str(x))
        elif dir=='L':
            # print('x0',str(x))
            # print('dist',str(d))
            process_row_move(map,x-d,x,y)
            x=x-d
            # print('x1',str(x))
        elif dir=='U':
            print('y0',str(y))
            print('dist',str(d))
            process_column_move(map, x, y, y+d)
            y=y+d
            print('y1',str(y))
        else:
            print('y0',str(y))
            print('dist',str(d))
            process_column_move(map, x, y-d, y)
            y=y-d
            print('y1',str(y))

def process_row_move(map, x1, x2, y):
    for x in range(x1, x2):
        if map[x, y]==0:
            map[x,y]=1
        elif map[x,y]==1:
            map[x,y]=2
        else:
            print('Encoutered an unexpected value ',str(map[x,y]))
    
def process_column_move(map, x, y1, y2):
    for y in range(y1, y2):
        if map[x, y]==0:
            map[x,y]=1
        elif map[x,y]==1:
            map[x,y]=2
        else:
            print('Encoutered an unexpected value ',str(map[x,y]))


trace_wire_path(wires_map, dirs_red, dist_red)   
trace_wire_path(wires_map, dirs_blue, dist_blue)   
# print(np.nonzero(wires_map))
(int_rows, int_cols)=np.where(wires_map==2)

# fig = pyplot.figure(figsize=(6, 3.2))
# ax = fig.add_subplot(111)
# ax.set_title('WiresMap')
pyplot.imshow(wires_map)
# ax.set_aspect('equal')
pyplot.show()
# pyplot.matshow(wires_map)

# def calc_closest_intersect(rows, cols):
#     dist_to_origin = 10e7
#     for i in range(len(rows)):
#         d = abs(rows[i]-1001)+abs(cols[i]-1001)
#         if d<dist_to_origin:
#             dist_to_origin=d
#     return dist_to_origin

# d = calc_closest_intersect(int_rows, int_cols)
# print(d)    
