def select_sort(alist):    
    for j in range(len(alist)-1):
        min_index =j
        for i in range(j+1,len(alist)):
            if alist[min_index] > alist[i]:
                min_index=i
            alist[j],alist[min_index] =alist[min_index],alist[j]
            print(alist)


new_list =select_sort([21,345,673,3,123,234,67,5,3,1,534,5676,223,23,57,9,67,34212,34,7,43])
print(new_list)    