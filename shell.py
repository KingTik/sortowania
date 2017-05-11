import numpy
import math
import copy
def shellSort(tablica):
    
    N = len(tablica)
    h = int(math.floor(N/2))


    while h >= 1:
        
        
        for i in range (0, N-h):
            done = False
            j = i
            while(done == False):
                
                if tablica[j] > tablica[j+h]:
                    tmp = tablica[j]
                    tablica[j] = tablica[j+h]
                    tablica[j+h] = tmp
                
                if j-h >= 0:
                    j = j-h
                else:
                    done = True
                

        h = h = int(math.floor(h/2))


    return tablica






for i in range(0, 1000):

    tab = [int(99*numpy.random.random()) for i in xrange(int(999*numpy.random.random()))]
    prev = copy.deepcopy(tab)
    szel = shellSort(tab)
    prev.sort()


    if prev == szel:
        pass
    else:
        print 'rozne'
        print prev
        print szel
        break