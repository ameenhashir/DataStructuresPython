def shell_sort(elements):
    size = len(elements)
    gap = size // 2
    while gap > 0:
        for i in range(gap,size,gap):
            anchor = elements[i]
            j = i - gap
            while j>=0 and elements[j] > anchor:
                elements[j + gap] = elements[j]
                j -= gap
            elements[j + gap] = anchor
        gap = gap//2

if __name__=='__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5]
    ]
    for elements in tests:
        shell_sort(elements)
        print(elements)