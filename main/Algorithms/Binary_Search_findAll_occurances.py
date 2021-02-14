import time

def binary_search(element_list, find_element, start=0, end=None):
    left_index = start
    right_index = len(element_list) - 1 if not end else end
    mid_index = (left_index + right_index) // 2
    found_indx_list = []
    if left_index <= right_index:
        if element_list[mid_index] == find_element:
            return mid_index
        elif element_list[mid_index] > find_element:
            return binary_search(element_list, find_element, left_index, mid_index - 1)
        else:
            return binary_search(element_list, find_element, mid_index + 1, right_index)
    return -1


def find_all_occurances(elements, find_element):
    index = binary_search(elements, find_element)
    found_index_list = []
    if index == -1:
        return []
    else:
        found_index_list.append(index)
        right_index = index + 1
        left_index = index - 1
        while elements[right_index] == find_element and right_index < len(elements):
            found_index_list.append(right_index)
            right_index += 1
        while elements[left_index] == find_element and left_index > 0:
            found_index_list.append(left_index)
            left_index -= 1
        return sorted(found_index_list)


if __name__ == "__main__":
    elements = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    find_element = 15

    ts = time.time()
    bs = binary_search(elements, find_element)
    print('%r  %2.2f ms' % (binary_search.__name__, (time.time() - ts) * 1000))
    print("Binary Search : Element {} found at index {}".format(find_element, bs))

    print("Binary Search All Accurances: Element {} found at indexes {}".format(find_element,find_all_occurances(elements,find_element)))