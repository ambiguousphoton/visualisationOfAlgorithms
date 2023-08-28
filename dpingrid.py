# rows = 15
# grid = [
#         [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#        ]

def depth_first_search(row, col, rows, grid, end, memory = None):
    if memory == None:
        memory = {}
    if (row,col) in memory:
        return memory[(row,col)] 
    
    if grid[row][col] == end:
        memory[(row,col)] = []
        return []
    
    memory[(row,col)] = None
    path_found = None
    if row + 1 < rows: # search down
        path =  depth_first_search( row + 1, col, rows, grid, end, memory)
        if path != None and path_found == None:
            path_found = True
            path.append((row,col))
            memory[(row, col)] = path.copy()
    if col + 1 < rows: # search right
        path = depth_first_search(row, col + 1, rows, grid, end, memory)
        if path != None and path_found == None:
            path_found = True
            path.append((row,col))
            memory[(row,col)] = path.copy()
    if row - 1 > -1:   # search up
        path = depth_first_search(row - 1, col, rows, grid, end, memory)
        if path != None and path_found == None:
            path_found = True
            path.append((row,col))
            memory[(row,col)] = path.copy()
    if col - 1 > - 1:   # search left
        path = depth_first_search(row, col - 1, rows, grid, end, memory)
        if path != None and path_found == None:
            path_found = True
            path.append((row,col))
            memory[(row, col)] = path.copy()
    
    return memory[(row,col)]

# result = depth_first_search(0,0,rows,grid,1)
# print(result)

# grid2 = []
# for i in range(15): 
#     row  = []
#     for j in range(15):
#         row.append(0)
#     grid2.append(row)
# for i in result:
#     grid2[i[0]][i[1]] = 'i'

# for i in grid2:
#     print(i)
    