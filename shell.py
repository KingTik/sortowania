import numpy
import math
import copy
def shellSort(tablica):
    """ shell sort"""
    N = len(tablica)
    h = int(math.floor(N/2)) #rozstaw


    while h >= 1:
        
        
        for i in range (0, N-h): # przejscie 'w przod' tablicy
            done = False
            j = i
            while(done == False):   #jezeli jest potrzeba przejscie 'w tyl' tablicy w celu znalezienia odpowiedniego miejsca
                
                if tablica[j] > tablica[j+h]:
                    #podmiana
                    tmp = tablica[j]
                    tablica[j] = tablica[j+h]
                    tablica[j+h] = tmp
                
                if j-h >= 0:    #przestawienie porownania o jeden rozstaw w tyl
                    j = j-h
                else:
                    done = True #znaleziono miejsce
                

        h = h = int(math.floor(h/2)) #zmniejszenie rozstawu


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