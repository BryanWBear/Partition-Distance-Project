import random

def partitionParser(string):
    new_partition = False
    string_list = []
    for x in string:
        if x == '}':
            new_partition = False
            string_list.append(new_string)
        if new_partition is True:
            new_string = new_string+x
        if x == '{':
            new_string = ''
            new_partition = True
    partition_list = []
    count = 0
    for x in string_list:
        partition_list.append(x.split())
    return partition_list
            
def createAssignmentMatrix(partition1, partition2):
    p1 = partitionParser(partition1)
    p2 = partitionParser(partition2)
    matrix = []
    count = 0
    current = 0
    for x in p1:
        row = []
        for y in p2:
            for z in x:
                for w in y:
                    if z==w:
                        current+=1
            row.append(current)
            current = 0
        matrix.append(row)
    return matrix
                
def badAssignmentAlg(matrix):
    n = len(matrix)
    tmatrix = transpositionGen(n)
    usedt = []
    initialp = []   
    for x in range(0, n):
        initialp.append(x+1)
    max_assignment = 0
    max_config = []
    currentstate = [] 
    while(currentstate != initialp and len(tmatrix)!=0):
        if currentstate == []:
            currentstate=initialp[:]
        current_assignment = computeAssignment(matrix, currentstate)
        if current_assignment > max_assignment:
            max_assignment = current_assignment
            max_config = currentstate[:]
        if len(tmatrix) > 1:
            current_t = tmatrix.pop(random.randrange(0, len(tmatrix))) #pick a random transposition, use it, and delete it from the list   
        else:
            current_t = tmatrix.pop()
        usedt.append(current_t)
        i = current_t[0]
        j = current_t[1]
        currentstate[i-1], currentstate[j-1] = currentstate[j-1], currentstate[i-1]
        print(currentstate)
        print(max_config)
    return max_assignment
    
def greedyAlg(matrix):
    max_assignment = []
    while len(matrix)!= 0:
        maxlist = []
        for row in matrix:
            maxlist.append(max(row))
        maxval = max(maxlist)
        max_assignment.append(maxval)
        maxindex = maxlist.index(maxval)
        colindex = matrix[maxindex].index(maxval)
        matrix = newMatrix(matrix, colindex, maxindex)[:]
    return max_assignment
       
def newMatrix(matrix,n, m): #returns a matrix missing the mth row and nth column. 
    l = len(matrix)
    for x in range(0,l):
        matrix[x].pop(n)
    matrix.pop(m)
    return matrix 
            
def randomMatrixGenerator(size, num = 5):
    matrix = []
    for x in range(0, size):
        matrix.append([0]*size)
    path = pathGenerator(size)
    values = randomIntersects(num, 2*size-1)
    for coordinate in path:
        matrix[coordinate[0]][coordinate[1]] = values.pop(-1)
    return matrix    
        
def pathGenerator(size):
    path = []
    current = (0,0)
    path.append(current)
    onwall = False
    while current!=(size-1, size-1):
        direction = random.randint(1, 2)
        if onwall==True:
            if current[0]==size-1:
                current = (current[0], current[1]+1)
            else:
                current = (current[0]+1, current[1])               
        else:
            if direction==1:
                current = (current[0]+1, current[1])
            else:
                current = (current[0], current[1]+1)
        if current[0]==size-1 or current[1]==size-1:
            onwall = True
        path.append(current)
    return path
    
def randomIntersects(size, num): #randomPartition but can generate 0
    partition = []
    for x in range(0, num):
        threshold = size - (num - x)
        if x>=threshold and x!=num-1:
            rnum = 1
        elif size > 0 and x==num-1:
            rnum = size
        else:
            rnum = random.randrange(0, threshold)
        partition.append(rnum)
        size-=rnum
    return partition

def randomPartition(size, num):
    partition = []
    for x in range(0, num):
        threshold = size - (num - x)
        if x>=threshold and x!=num-1:
            rnum = 1
        elif size > 0 and x==num-1:
            rnum = size
        else:
            rnum = random.randrange(1, threshold)
        partition.append(rnum)
        size-=rnum
    return partition
    
def computeAssignment(matrix, permutation):
    sum = 0
    for x in range(0, len(permutation)):
        sum+=matrix[permutation[x]-1][x]
    return sum
    
def transpositionGen(n):
    tmatrix = []
    for x in range(1,n+1):
        for y in range(x+1, n+1):
            tmatrix.append([x,y])
    return tmatrix
    
#def cycleComposer(cycle_matrix):
    
    