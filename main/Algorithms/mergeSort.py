def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge_array(left,right,arr)


def merge_array(left,right,arr):
    i,j,k=0,0,0
    while i < len(left) or j < len(right):
        if i < len(left) and j <len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
        elif i < len(left):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1


if __name__=='__main__':
    elements = [[10, 20, 1, 3, 4, 89, 50], [10], [50, 1], [1, 2, 3, 4, 5], []]
    for elem in elements:
        merge_sort(elem)
        print(elem)