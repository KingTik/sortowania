import numpy
import math
import copy

def insertSort(tablica):
    
    N = len(tablica)

    for i in range(1, N):
        tmp = tablica.pop(i)
        j = i-1
        while(j>=0):
            if tablica[j] < tmp:
                tablica.insert(j+1, tmp)
                break
            if j==0:
                tablica.insert(0, tmp)
            j-=1

    return tablica






for i in range(0, 1000):

    tab = [int(99*numpy.random.random()) for i in xrange(int(999*numpy.random.random()))]
    prev = copy.deepcopy(tab)
    szel = insertSort(tab)
    prev.sort()


    if prev == szel:
        pass
    else:
        print 'rozne'
        print prev
        print szel
        break