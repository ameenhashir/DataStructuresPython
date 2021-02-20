def index_to_insert(array,num):
    j = len(array)-1
    while j >= 0 and num < array[j]:
        j -= 1
    return j + 1

def input_to_stream(array,num):
    idx = index_to_insert(array,num)
    array.insert(idx,num)
    return array


if __name__=='__main__':
    stream = []
    count = 0
    while True:
        num = int(input("Enter Number (-1 to terminate) : "))
        if num == -1:
            break
        count +=1
        stream = input_to_stream(stream,num)
        print(stream)
        l = len(stream)
        if l % 2 != 0:
            print(f"Median is {stream[l//2]}")
        else:
            print(f"Median is {(stream[(l//2) - 1] + stream[(l//2)])/2}")