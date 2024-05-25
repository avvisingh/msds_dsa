def merge_op(arr, p, q, r):
    left_len = q-p+1 #[p...q]
    right_len = r-q #[q+1...r]
    left_arr = []
    right_arr = []

    for i in range(left_len):
        left_arr.insert(i, arr[p+i])
    for j in range(right_len):
        right_arr.insert(j, arr[q+j+1])
    
    i = 0
    j = 0
    k = p

    while i < left_len and j < right_len:
        if left_arr[i] <= right_arr[i]:
            arr[k] = left_arr[i]
            i+=1
        else:
            arr[k] = right_arr[j]
            j+=1
        k+=1
    
    while i < left_len:
        arr[k] = left_arr[i]
        i+=1
        k+=1
    while j < right_len:
        arr[k] = right_arr[j]
        j+=1
        k+=1
    
    print(arr)

my_array = [6, 7, 8, 9, 10, 1, 2, 3, 4]

# merge_op(my_array, 0, 4, (len(my_array)-1))

def merge_lists(lst1, lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    if n1 == 0:
        return list(lst2)
    elif n2 == 0:
        return list(lst1)
    else:
        output_list = []
        i = 0
        j = 0
        while i < n1 and j < n2:
            if lst1[i] <= lst2[j]:
                output_list.append(lst1[i])
                i+=1
            else:
                output_list.append(lst2[j])
                j+=1
        while i < n1:
            output_list.append(lst1[i])
            i+=1
        while j < n2:
            output_list.append(lst2[j])
            j+=1
        return output_list
    
##### I AM COPYING THE BELOW DIRECTLY FROM THE MERGE SORT JUPYTER NOTEBOOK #####
    
def swap_els(lst, i, j):
    n = len(lst)
    assert(i >= 0 and i < n)
    assert(j >= 0 and j < n)
    (lst[i], lst[j]) = (lst[j], lst[i])
    return

lst1 = [30, 33, 44, 45, 56, 67]
lst2 = [2, 7, 11, 15, 16, 21, 22, 23, 24, 25, 26, 27, 27]

# out = merge_lists(lst1, lst2)
# print(out)

test_swap = [0, 10]
swap_els(test_swap, 0, 1)
print(test_swap)

def copy_back(output_lst, lst, left, right):
    assert(len(output_lst) == right - left + 1)
    for i in range(left, right+1):
        lst[i] = output_lst[i - left]
    return

def mergeHelper(lst, left, mid, right):
    #Perform a merge on sublists lst[left: mid+1] and lst[mid+1: right]
    if left > mid or mid > right: #one of the 2 sublists is empty
        return
    i1 = left
    i2 = mid + 1
    output_lst = []
    while (i1 <= mid or i2 <= right):
        if (i1 <= mid and i2 <= right):
            if lst[i1] <= lst[i2]:
                output_lst.append(lst[i1])
                i1 += 1
            else:
                output_lst.append(lst[i2])
                i2 += 1
        elif i1 <= mid:
            output_lst.append(lst[i1])
            i1 += 1
        else:
            output_lst.append(lst[i2])
            i2 += 1
    copy_back(output_lst, lst, left, right)
    return

#Function mergeSortHelper
#recursive implementation of mergeSort
def mergeSortHelper(lst, left, right):
    if (left == right): #Region to sort is a singleton - a one element is already sorted by default
        return
    elif (left + 1 == right): #region to sort has 2 elements - swap if needed
        if (lst[left] > lst[right]):
            swap_els(lst, left, right)
    else:
        mid = (left + right) // 2
        mergeSortHelper(lst, left, mid)
        mergeSortHelper(lst, mid + 1, right) #Recursively sort both the left and half lists
        mergeHelper(lst, left, mid, right)

#Function mergesort
# Sort the list in place and modify it so that 
# lst is sorted when the function returns
def mergeSort(lst):
    if len(lst) <= 1:
        return # nothing to do
    else:
        mergeSortHelper(lst, 0, len(lst)-1)