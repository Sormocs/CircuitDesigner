# Shell sort
def shellSort(array, n):

    # Rearrange elements at intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


data = input('Enter the list of numbers separated by space\n').split()
data = [int(x) for x in data]
shellSort(data, len(data))
print('Sorted Array in Ascending Order:', data)