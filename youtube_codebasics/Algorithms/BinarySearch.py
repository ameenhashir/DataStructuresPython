import time

def linear_search(elements,search_elem):
    for idx,elem in enumerate(elements):
        if elem == search_elem:
            return idx
    return -1

def binary_search(element_list,find_element,start =0,end = None):
    left_index= start
    right_index = len(element_list)-1 if not end else end
    mid_index = (left_index + right_index)//2
    if left_index <= right_index:
        if element_list[mid_index] == find_element:
            return mid_index
        elif element_list[mid_index] > find_element:
            return binary_search(element_list,find_element,left_index,mid_index-1)
        else:
            return binary_search(element_list,find_element,mid_index+1,right_index)
    return -1

if __name__=="__main__":
    elements = [i for i in range(0,1000000,2)]
    find_element = 999998
    ts = time.time()
    ls = linear_search(elements, find_element)
    print('%r  %2.2f ms' %(linear_search.__name__, (time.time() - ts) * 1000))
    print("Linear Search : Element {} found at index {}".format(find_element,ls))

    ts = time.time()
    bs = binary_search(elements, find_element)
    print('%r  %2.2f ms' % (binary_search.__name__, (time.time() - ts) * 1000))
    print("Binary Search : Element {} found at index {}".format(find_element,bs))