import random
import numpy
import scipy.special
import sys
import itertools
#from munkres import Munkres

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
    for x in range(0, min(len(matrix), len(matrix[0]))):
        maxlist = [max(row) for row in matrix]
        maxval = max(maxlist)
        max_assignment.append(maxval)
        maxindex = maxlist.index(maxval)
        colindex = matrix[maxindex].index(maxval)
        matrix = newMatrix(matrix, colindex, maxindex)[:]
    return sum(max_assignment)
    
def sortedGAlg(matrix):
    maxlist = []
    mlist = matrixSort(matrix)
    
    while(len(maxlist) < n):
        if(maxlist == []):
            maxlist.append(mlist.pop())
            clist = [s[1:2] for s in mlist]
        current = mlist.pop()
        
def matrixSort(matrix):
    rowsize = len(matrix[0])
    sortlist = addLists(matrix)
    for i in range(len(sortlist)):
        sortlist[i] = (sortlist[i], i/rowsize, i%rowsize)
    return sorted(sortlist, key=lambda entry: entry[0])
    
def addLists(matrix):
    if(len(matrix)==0):
        return []
    else:
        return matrix.pop(0)+addLists(matrix)
    
    
def munkresAlg(matrix): #code taken from python.org
    cost_matrix = []
    for row in matrix:
        cost_row = []
        for col in row:
            cost_row += [sys.maxsize - col]
        cost_matrix += [cost_row]
    m = Munkres()
    indexes = m.compute(cost_matrix)
    total = 0
    for row, column in indexes:
        value = matrix[row][column]
        total += value
    return total
       
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
    
def dirichlet(n, theta = 3, alpha = 0):
    """
    n = size of set you're sampling from
    theta = concentration parameter
    alpha = "discount" parameter
    """
    theta = float(theta)
    list = []
    for x in range(n):
        #P(a) = putting elt into new subset
        #P(b) = putting elt into existing subset
        z = x + theta
        probs = [float(len(s))-alpha for s in list]
        probs += [theta + len(list)*alpha]
        probs = [y/z for y in probs]
        rand = random.uniform(0.,1.)
        for j,elt in enumerate(probs):
            rand-=elt
            if rand < 0:
                if j < len(list):
                    list[j].append(x)
                else:
                    list.append([x]) 
                break
    return list

def exp_nc(n=100,theta=1.,alpha=0.):
    s='Expected number of clusters for'
    s+=' n=' + str(n)
    s+=' theta=' + str(theta)
    s+=' alpha=' + str(alpha)
    print s

    if alpha > 0.:
        n1 = scipy.special.gamma(theta+n+alpha)
        n2 = scipy.special.gamma(theta+1)
        n3 = scipy.special.gamma(theta+n)
        n4 = scipy.special.gamma(theta+alpha)
        return( n1*n2 / ( alpha*n3*n4 ) - theta/alpha )

    elif alpha == 0.:
        v = 0.
        for k in range(n):
            v += theta / (theta + k)
        #v = sum([ (theta/(theta+k-1.)) for k in range(n)])
        return(v)



def matrixGenerator(p1, p2):
    matrix = []
    for x in range(len(p1)):
        current = p1[x]
        ilist = [set(s).intersection(current) for s in p2]
        matrix.append([len(s) for s in ilist])       
    return matrix
    
def testMain(n, p1, p2): #n = number of trials, p1 and p2 = dirichlet parameters
    success = 0.0
    diff = 0.0
    diffcount = 0
    for x in range(0, n):
        part1 = dirichlet(p1[0], p1[1], p1[2])
        part2 = dirichlet(p2[0], p2[1], p2[2])
        matrix = matrixGenerator(part1, part2)
        a2 = munkresAlg(matrix)
        a1 = greedyAlg(matrix)
        if a1==a2:
            success+=1
        else:
            diff+=abs(a1 - a2)
            diffcount+=1
    return (success/n, diff/diffcount)
    
### simulation

def sim_dpp_batch(rep=1, n=[10,100], theta=[1.0,2.0], alpha=[0.0,0.1]):

    v = [ n, theta, alpha ]
    params = list(itertools.product(*v))
    m = {}
    for i in params:
        m[i] = []
        for r in range(rep):
            m[i].append(dirichlet(n=i[0], theta=i[1], alpha=i[2]))
    return m

def plot_vars():
    # http://stackoverflow.com/questions/7941207/is-there-a-function-to-make-scatterplot-matrices-in-matplotlib
    # wow, it really works!
    return
