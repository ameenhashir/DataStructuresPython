def insertion_sort(elements):
    for i in range(1,len(elements)):
        anchor = elements[i]
        j = i - 1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j -=1
        elements[j+1] = anchor


if __name__ == '__main__':
    elements = [[10,20,1,3,4,89,50],[10],[50,1],[1,2,3,4,5],[]]
    for elem in elements:
        insertion_sort(elem)
        print(elem)