# Dp Non recursive
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
