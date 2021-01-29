# Shell sort
def SortUp(array,names):
    new = []
    for n in array:
        new.append(int(n))
    array = new
    def shellSort(array, n, names):

        # Rearrange elements at intervals
        interval = n // 2
        while interval > 0:
            for i in range(interval, n):
                temp0 = names[i]
                temp = array[i]
                j = i
                while j >= interval and array[j - interval] > temp:
                    names[j] = names[j - interval]
                    array[j] = array[j - interval]
                    j -= interval

                names[j] = temp0
                array[j] = temp
            interval //= 2


    shellSort(array, len(array), names)
    array.reverse()
    names.reverse()
    return [array,names]