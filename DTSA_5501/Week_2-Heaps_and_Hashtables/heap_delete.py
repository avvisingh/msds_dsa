from bubble_down import bubble_down_func
from bubble_up import bubble_up_func

# Min Heaps to use for testing
# [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
# [-14, -8, -6, 1, 7, 13, 18, 21, 27, 32]
# [-13, -7, -2, 3, 9, 14, 19, 24, 29, 34]
# [-12, -9, -4, 2, 6, 11, 17, 22, 26, 31]
# [-11, -6, -1, 4, 8, 12, 16, 23, 28, 33]
# [-15, -12, -9, -6, -3, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
# [-14, -11, -8, -5, -2, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
# [-13, -10, -7, -4, -1, 2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
# [-12, -9, -6, -3, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# [-11, -8, -5, -2, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31]

# Max Heaps to use for testing
# [30, 25, 20, 15, 10, 5, 0, -5, -10, -15]
# [32, 27, 21, 18, 13, 7, 1, -6, -8, -14]
# [34, 29, 24, 19, 14, 9, 3, -2, -7, -13]
# [31, 26, 22, 17, 11, 6, 2, -4, -9, -12]
# [33, 28, 23, 16, 12, 8, 4, -1, -6, -11]
# [27, 24, 21, 18, 15, 12, 9, 6, 3, 0, -3, -6, -9, -12, -15]
# [28, 25, 22, 19, 16, 13, 10, 7, 4, 1, -2, -5, -8, -11, -14]
# [29, 26, 23, 20, 17, 14, 11, 8, 5, 2, -1, -4, -7, -10, -13]
# [30, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0, -3, -6, -9, -12]
# [31, 28, 25, 22, 19, 16, 13, 10, 7, 4, 1, -2, -5, -8, -11]

test_arr = [40, 1, 39, -1, 1, 38, 37, -2, -3, 0, -4, 37, 36, 36, 35, -100]
print(f'Testing with the following heap: {test_arr}')

def heap_delete(arr, j, heap):
  if j == len(arr):
    arr.pop()
    return
  
  arr[j-1] = arr[-1]
  arr.pop()
  
  if j == 1:
    # Element deleted was root element - only need to bubble down.
    bubble_down_func(arr, j, heap)
  else:
    parent = j//2
    left_child = j*2 if j*2 <= len(arr) else None
    right_child = left_child+1 if left_child != None else None

    if left_child == None: # Element deleted has no children (is a leaf) - only need to bubble up
      bubble_up_func(arr, j, heap)
    else:
      if heap.lower() == 'min':
        if arr[j-1] < arr[parent-1]:
          bubble_up_func(arr, j, heap)
        else:
          bubble_down_func(arr, j, heap)
      else:
        if arr[j-1] > arr[parent-1]:
          bubble_up_func(arr, j, heap)
        else:
          bubble_down_func(arr, j, heap)



heap_delete(test_arr[:15], 1, 'max')
print(f'Bubble Down completed. Output: {test_arr}')