# Quick Sort
def quick_sort(alist, start, end):
    # Sorts the list from indexes
    if end - start > 1:
        p = partition(alist, start, end)
        quick_sort(alist, start, p)
        quick_sort(alist, p + 1, end)


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j


nlist = input('Enter the list of numbers separated by space\n').split()
nlist = [int(x) for x in nlist]
quick_sort(nlist, 0, len(nlist))
nlist.reverse()
print('Sorted List after Quick Sort, in Descending Order\n', nlist)