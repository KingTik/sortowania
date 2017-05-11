import numpy
import math
import copy
def bubbleSort(tablica):
    """ sortowanie bombelkowe """
    for i in range(0, len(tablica)-1): #pierwsza petla
        for n in range(0, len(tablica)-1-i): #druga petla pomniejszona o posortowana czesc
            if tablica[n] > tablica[n+1]:
                tmp = tablica[n]
                tablica[n] = tablica[n+1]
                tablica[n+1] = tmp
    
    return tablica




for i in range(0, 1000):
    
    tab = [int(99*numpy.random.random()) for i in xrange(int(999*numpy.random.random()))]
    prev = copy.deepcopy(tab)
    szel = bubbleSort(tab)
    prev.sort()


    if prev == szel:
        pass
    else:
        print 'rozne'
        print prev
        print szel
        break
