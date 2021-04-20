def selection_sort(array):
    size = len(array)
    for i in range(size-1):
        j = i
        min_elem = array[i]
        m = i
        while j < size:
            if min_elem > array[j]:
                min_elem = array[j]
                m = j
            j += 1
        if m != i:
            array[m],array[i] = array[i],array[m]


if __name__=='__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5]
    ]
    for elements in tests:
        selection_sort(elements)
        print(elements)