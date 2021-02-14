def swap(elements,pos1,pos2):
    elements[pos1],elements[pos2] = elements[pos2],elements[pos1]


def partition(elements,start,end):
    pivot = start
    start_index = start + 1
    end_index=end

    while start_index < end_index:
        while elements[pivot] > elements[start_index] and start_index < len(elements):
            start_index += 1
        while elements[pivot] < elements[end_index] and end_index > 0:
            end_index -= 1
        if start_index < end_index:
            swap(elements,start_index,end_index)
    swap(elements, pivot, end_index)
    return end_index


def quick_sort(elements,start,end):
    if start < end:
        pivot_index = partition(elements,start,end)
        quick_sort(elements,start,pivot_index-1)
        quick_sort(elements, pivot_index + 1,end)


if __name__ == '__main__':
    elements = [[10,20,1,3,4,89,50],[10],[50,1],[1,2,3,4,5]]
    for elem in elements:
        quick_sort(elem,0,len(elem)-1)
        print(elem)
