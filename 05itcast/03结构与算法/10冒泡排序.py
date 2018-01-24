def bubble_sort(alist):
    for j in range(len(alist)-1):
        for i in range(len(alist)-1):
            if alist[i] >alist[i+1]:
                temp =alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp
    print(alist)            



new_list =bubble_sort([21,345,673,3,123,234,67,5,3,1,534,5676,223,23,57,9,67,34212,34,7,43])
print(new_list)    