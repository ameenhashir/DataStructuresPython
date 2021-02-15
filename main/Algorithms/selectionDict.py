def selection_sort(array,keys):
    size = len(array)
    for key in keys[::-1]:
        for i in range(size-1):
            j = i
            min_elem = (i,array[i])
            while j < size:
                if min_elem[1][key] > array[j][key]:
                    min_elem = (j,array[j])
                j += 1
            if min_elem[0] != i:
                array[min_elem[0]],array[i] = array[i],array[min_elem[0]]



if __name__=='__main__':
    elements = [{'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}]
    selection_sort(elements,keys=["First Name",'Last Name'])
    for elem in elements:
        print(elem)