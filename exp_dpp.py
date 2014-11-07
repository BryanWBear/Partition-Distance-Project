import numpy
import scipy.special

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

