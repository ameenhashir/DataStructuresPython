class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for x in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for l in key:
            h += ord(l)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] is None or self.arr[h][0] == key:
            self.arr[h] = (key,value)
            return
        else:
            i = self.MAX
            while i > 0:
                h = (h + 1)%self.MAX
                if self.arr[h] is None:
                    self.arr[h] = (key, value)
                    return
                i -= 1
            if i == 0:
                raise Exception("Hash Table is Full!!!")

    def __getitem__(self, item):
        h = self.get_hash(item)
        if self.arr[h][0] == item:
            return self.arr[h][1]
        else:
            i = self.MAX
            while i > 0:
                h = (h + 1) % self.MAX
                if self.arr[h][0] == item:
                    return self.arr[h][1]
                i -= 1
            if i == 0:
                raise Exception("Key Not Found")

    def __delitem__(self, item):
        h = self.get_hash(item)
        if self.arr[h][0] == item:
            self.arr[h] = None
            return
        else:
            i = self.MAX
            while i > 0:
                h = (h + 1) % self.MAX
                if self.arr[h][0] == item:
                    self.arr[h]=None
                    return
                i -= 1
            if i == 0:
                raise Exception("Key Not Found")

if __name__=='__main__':
    h= HashTable()
    h['march 6'] = 290
    h['march 6'] = 300
    h['march 7'] = 400
    h['march 8'] = 500
    h['march 9'] = 600
    h['march 10'] = 700
    h['march 11'] = 800
    h['march 12'] = 900
    h['march 13'] = 1000
    h['march 14'] = 2000
    h['march 15'] = 5000
 #  h['march 16'] = 50000
    print(h.arr)
    print(h['march 9'])
 #  print(h['march 19'])
    del h['march 11']
    print(h.arr)