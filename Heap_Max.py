class Heap:
    def __init__(self):
        self._array = []
        self._root = None

    def search(self,data):
        if data in self._array:
            return True
        else:
            return False

    #gets index counting from last
    def getindex(self,data):
        if self.search(data) == True:
            lent = len(self._array)
            LIST = self._array
            LIST.reverse()
            c = lent - 1
            for i in LIST:
                if i == data:
                    LIST.reverse()
                    return c
                else:
                    c -= 1
        else:
            print(data,"does not exist in Heap")      

    def swap(self,a,b):
        if self.search(a) == True or self.search(b) == True:
            indexa = self.getindex(a)
            indexb = self.getindex(b)
            self._array[indexa] = b
            self._array[indexb] = a
        else:
            print(a,'or',b,"do not exist in Heap")

    def print(self):
        print(self._array)

    def getmax(self):
        return self._root

    #Searches from start of Array
    def getparent(self,data):
        if self.search(data) == True:
            indexdata = self.getindex(data)
            indexparent = int((indexdata - 1) / 2)
            return self._array[indexparent]
        else:
            print(data,"does not exist in Heap")

    def getleft(self,data):
        if self.search(data) == True:
            indexdata = self.getindex(data)
            indexleft = int((2 * indexdata) + 1)
            if indexleft >= len(self._array):
                return None
            else:
                return self._array[indexleft]
        else:
            print(data,"does not exist in Heap")

    def getright(self,data):
        if self.search(data) == True:
            indexdata = self.getindex(data)
            indexright = int((2 * indexdata) + 2)
            if indexright >= len(self._array):
                return None
            return self._array[indexright]
        else:
            print(data,"does not exist in Heap")

    def haschild(self,data):
        if self.search(data) == True:
            if self.getleft(data) != None or self.getright(data) != None:
                return True
            else:
                return False
        else:
            print(data,"does not exist in Heap")

    def maxchild(self,data):
        if self.haschild(data) == True:
            if self.getright(data) == None:
                return self.getleft(data)
            if self.getleft(data) > self.getright(data):
                return self.getleft(data)
            else:
                return self.getright(data)
        else:
            return None

    def insert(self,data):
        self._array.append(data)
        node = data
        while node > self.getparent(node):
            self.swap(self.getparent(node),node)
        self._root = self._array[0]

    def delete(self,data):
        if self.search(data) == True:
            initialindex = self.getindex(data)
            arraylength = len(self._array)
            self.swap(data,self._array[arraylength-1])
            del self._array[arraylength-1]
            if len(self._array) != 0:
                node = self._array[initialindex]
                while self.maxchild(node) != None  and node < self.maxchild(node):
                    self.swap(node,self.maxchild(node))
                self._root = self._array[0]
            else:
                self._root = None
        else:
            print(data,"does not exist in Heap")

    def push(self,data):
        self.insert(data)
    
    def pop(self):
        print(self._root)
        self.delete(self._root)

    def heapsort(self):
        LIST = []
        while len(self._array) != 0:
            LIST.append(self._root)
            self.delete(self._root)
        return LIST

    def heapify(self,LIST):
        for i in LIST:
            self.insert(i)  

##################################################################################
H = Heap()
H.insert(90)
H.insert(89)
H.insert(70)
H.insert(36)
H.insert(75)
H.insert(63)
H.insert(65)
H.insert(21)
H.insert(18)
H.insert(15)
H.insert(12)
#H.insert(89)
#H.delete(89)
#H.delete(90)
H.print()
#H.heapsort()
#H.heapify(H.heapsort())











    

