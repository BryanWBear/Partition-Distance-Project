import random

def sim_mixture_normal(n,p=[(0.,1.,1.)]):
   
    k = len(p)
    # vector of iid observations
    x = [] 

    # unnormalized sampling weights from mixture of normals
    w = [ i[2] for i in p ]
    print(w)

    # normalize those sampling weights
    w = [ float(i)/sum(w) for i in w ]
    print(w)

    for i in range(n):
        # sample mixture component j from w
        u = random.uniform(0,1)
        for j in range(k):
            u -= w[j]
            print j,u
            # found our mixture component
            if u <= 0.:
                x.append(random.gauss(mu=p[j][0],sigma=p[j][1]))
                break
    
    return(x)
