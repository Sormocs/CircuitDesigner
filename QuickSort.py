# Quick Sort

def SortDown(nlist,names):
    new = []
    for n in nlist:
        new.append(int(n))

    nlist = new
    def quick_sort(nlist,start, end,names):
        # Sorts the list from indexes
        if end - start > 1:
            p = partition(nlist,start, end,names)
            quick_sort(nlist,start, p,names)
            quick_sort(nlist,p + 1, end,names)

    def partition(nlist,start, end,names):

        pivot = nlist[start]
        i = start + 1
        j = end - 1

        while True:
            while (i <= j and nlist[i] <= pivot):
                i = i + 1
            while (i <= j and nlist[j] >= pivot):
                j = j - 1

            if i <= j:
                names[i], names[j] = names[j], names[i]
                nlist[i], nlist[j] = nlist[j], nlist[i]
            else:
                names[start], names[j] = names[j], names[start]
                nlist[start], nlist[j] = nlist[j], nlist[start]
                return j

    sorted = quick_sort(nlist,0,len(nlist),names)
    #nlist.reverse()
    #names.reverse()
    return [nlist,names]



# sorted = quick_sort(nlist, 0, len(nlist),names)
# nlist.reverse()
# names.reverse()
# print('Sorted List after Quick Sort, in Descending Order\n', nlist,'\n',names)

