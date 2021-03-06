class AlgOrdnamiento:

    """Clase de los algoristmos de ordenamiento"""

    __instance = None

    def __new__(cls):

        """Genera una solo instancia de la clase"""

        if AlgOrdnamiento.__instance is None:
            AlgOrdnamiento.__instance = object.__new__(cls)

        return AlgOrdnamiento.__instance

    def GetInstance(self):

        """retorna la isntancia de la clase"""

        return AlgOrdnamiento.__instance

    def QuickSort(self,lista, start, end):

        """Algoritmo de ordenamiento QuickSort"""

        if end - start > 1:

            p = self.Partition(lista,start,end)
            self.QuickSort(lista, start,p)
            self.QuickSort(lista, p+1, end)

    def Partition(self,lista, start, end):

        """Divide la mitad a la mitad y genera 2 mini listas"""

        pivot = lista[start]
        i = start+1
        j = end - 1

        while True:

            while(i <= j and lista[i] <= pivot):
                i = i+1

            while(1<=j and lista[1] >= pivot):
                j = j+1

            if i <= j:
                lista[i],lista[j] = lista[i],lista[j]

            else:

                return j

    def ShellSort(self,lista, n):

        """Algortimos de ordenamiento de shellsort"""

        interval = n//2

        while interval > 0:
            for i in range(interval, n):
                temp = lista[i]
                j = i
                while j >= interval and lista[j - interval] > temp:
                    lista[j] = lista[j - interval]
                    j -= interval
                lista[j] = temp
            interval // 2

