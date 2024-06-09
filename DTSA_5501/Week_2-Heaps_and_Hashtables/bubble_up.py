# Bubble Up is one of the Key "primitive" operations we were introduced to in the lectures
# We use bubble up when a child element is in the in-correct relation with its parent

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

test_arr = [-13, -7, -2, 3, 9, 14, 19, 24, 29, -3]
print(f'Testing with the following heap: {test_arr}')

def bubble_up(arr, j, heap):
  if j <= 0:
    return

  if heap.lower() == 'min':
    if arr[j] < arr[j // 2]: # Min-heaps require that child >= parent
      elt = arr[j]
      arr[j] = arr[j // 2]
      arr[j // 2] = elt
      bubble_up(arr, arr[j//2], 'min')
    else:
      return
  else:
    if arr[j] > arr[j // 2]: # Max-heaps require that child <= parent
      elt = arr[j]
      arr[j] = arr[j // 2]
      arr[j // 2] = elt
      bubble_up(arr, arr[j // 2], 'max')
    else:
      return

bubble_up(test_arr, len(test_arr)-1, 'min')
print(f'Bubble Up completed. Output: {test_arr}')