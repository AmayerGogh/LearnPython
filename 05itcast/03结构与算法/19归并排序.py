
def merge_sort(alist):
    '''
    归并排序
    '''
    n= len(alist)
    if n<=1:
        return alist
    mid=n//2
    #left 采用归并排序 形成有序的新列表
    left_li =merge_sort(alist[:mid])
    right_li =merge_sort(alist[mid:])
    #right 同
    left_pointer,right_pointer =0,0
    result =[]
    while left_pointer <len(left_li) and right_pointer <len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer +=1
        else:
            result.append(right_li[right_pointer])    
            right_pointer +=1
    result +=left_li[left_pointer:]
    result +=right_li[right_pointer:]     
    print(result)       
    return result


new_list =merge_sort([21,345,673,3,123,234,67,5,3,1,534,5676,223,23,57,9,67,34212,34,7,43])
print(new_list)