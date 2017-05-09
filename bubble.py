import numpy

def bubbleSort(tablica):
    """ sortowanie bombelkowe """
    for i in range(0, len(tablica)-1):
        for n in range(0, len(tablica)-1-i):
            if tablica[n] > tablica[n+1]:
                tmp = tablica[n]
                tablica[n] = tablica[n+1]
                tablica[n+1] = tmp
    
    return tablica





tab = [int(99*numpy.random.random()) for i in xrange(25)]

print tab
print bubbleSort(tab)

