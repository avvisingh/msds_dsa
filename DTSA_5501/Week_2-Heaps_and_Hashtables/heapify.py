from bubble_down import bubble_down_func
# TEST LISTS
# [12, -3, 25, 7, -15, 19, 4, 30, -8, 1]
# [5, -14, 27, 0, 15, -2, 22, -6, 18, 9]
# [20, 3, -7, 13, -10, 8, 30, -4, 11, 6]
# [-1, 24, 2, 9, 17, -5, 26, -12, 4, 15]
# [28, -9, 7, 10, -13, 19, 1, 23, 5, 14]
# [11, -6, 21, 3, 0, 18, -11, 29, 4, 8]
# [16, 2, -14, 25, -3, 12, 6, -7, 30, -2]
# [9, -5, 20, -8, 14, 27, 1, 5, -13, 22]
# [0, 13, 24, -10, 17, -1, 8, 29, 6, -15]
# [18, 4, -4, 10, 3, -9, 21, 7, 26, -12]

test_arr = [40, 1, 39, -1, 1, 38, 37, -2, -3, 0, -4, 37, 36, 36, 35, -100]
print(f'Testing with the following array: {test_arr}')

def heapify(arr, heap):
  heap_len = len(arr)
  print(f'heap_len = {heap_len}')
  last_parent = heap_len//2
  print(f'last_parent = {last_parent}')
  for i in range(last_parent, 0, -1):
    print(f'i = {i}')
    print(f'arr[i-1] = {arr[i-1]}')
    bubble_down_func(arr, i, heap)

heapify(test_arr, 'min')
print(f'Heapify completed. Output: {test_arr}')