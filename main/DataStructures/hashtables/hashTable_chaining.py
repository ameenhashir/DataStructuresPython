class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for x in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for l in key:
            h += ord(l)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        print(h)
        found = False
        for index,elem in enumerate(self.arr[h]):
            if elem[0] == key:
                self.arr[h][index] = (key,value)
                found = True
        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self, item):
        h = self.get_hash(item)
        found = False
        for elem in self.arr[h]:
            if elem[0] == item:
                return elem[1]
                found = True
        if not found:
            return "None"

    def __delitem__(self, key):
        h = self.get_hash(key)
        found = False
        for index,elem in enumerate(self.arr[h]):
            if elem[0] == key:
                del self.arr[h][index]
                return

if __name__=='__main__':
    h= HashTable()
    h['march 6'] = 290
    h['march 6'] = 300
    h['march 9'] = 190
    h['march 17'] = 1000
    print(h.arr)
    print(h['march 20'])
    print(h['march 6'])
    del h['march 6']
    print(h['march 6'])
    print(h.arr)