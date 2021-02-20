def merge_sort(arr,key=None,descending=False):
    if len(arr) >= 1 and key is None and isinstance(arr[0],dict):
        key = list(arr[0])[0]

    if len(arr) >= 1 and key in arr[0]:
        if len(arr) == 1:
            return
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left,key,descending)
        merge_sort(right,key,descending)
        merge_array(left,right,arr,key,descending)


def merge_array(left,right,arr,key,descending):
    i,j,k=0,0,0
    while i < len(left) or j < len(right):
        if i < len(left) and j <len(right):
            if not descending:
                if left[i][key] <= right[j][key]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
            else:
                if left[i][key] <= right[j][key]:
                    arr[k] = right[j]
                    j += 1
                else:
                    arr[k] = left[i]
                    i += 1
        elif i < len(left):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1


if __name__=='__main__':
    elements = [
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
    ]
    merge_sort(elements,key = 'time_hours',descending=True)
    print(elements)