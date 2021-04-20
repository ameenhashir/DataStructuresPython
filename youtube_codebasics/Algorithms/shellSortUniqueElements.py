def shell_sort(elements):
    size = len(elements)
    gap = size // 2
    del_index = set()
    while gap > 0:
        for i in range(gap,size,gap):
            anchor = elements[i]
            j = i - gap
            while j>=0 and elements[j] >= anchor:
                if elements[j] == anchor:
                    del_index.add(j)
                elements[j + gap] = elements[j]
                j -= gap
            elements[j + gap] = anchor
        gap = gap // 2
    for i,d in enumerate(del_index):
        del elements[d-i]


if __name__=='__main__':
    tests = [
        [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    ]
    for elements in tests:
        shell_sort(elements)
        print(elements)