def linear_search(elements,search_elem):
    for idx,elem in enumerate(elements):
        if elem == search_elem:
            return idx
    return -1

if __name__=="__main__":
    elements = [3,1,5,8,3,10,100,20,6]
    search = linear_search(elements,10)
    if search != -1:
        print('Element found at {} position'.format(search))
    else:
        print("Not Found")
