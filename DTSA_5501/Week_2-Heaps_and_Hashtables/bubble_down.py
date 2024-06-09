# Bubble Down is one of the Key "primitive" operations we were introduced to in the lectures
# We use bubble up when a parent element is in the wrong relation with its children elements

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

test_arr = [33, -7, -2, 3, 9, 14, 19, 24, 29, 34]
print(f'Testing with the following heap: {test_arr}')

def bubble_down(arr, j, heap):
  j+=1
  left_child = j*2
  right_child = j*2 + 1
  n = len(arr)

  if(left_child > n): # If True, then j has no children (is already a leaf)
    # In the lectures, we check for if left_child > n because we assume a 1-indexed heap for teaching purposes
    return
  
  if heap.lower() == 'min':
    if (left_child <= n) and (right_child > n): # If True, then j has only a left child and no right child
      if arr[j-1] > arr[left_child-1]:
        elt = arr[j-1]
        arr[j-1] = arr[left_child-1]
        arr[left_child-1] = elt
        return
    else:
      if arr[left_child-1] <= arr[right_child]-1: smallest = left_child
      else: smallest = right_child

      if arr[j-1] > arr[smallest-1]:
        elt = arr[j-1]
        arr[j-1] = arr[smallest-1]
        arr[smallest-1] = elt
        bubble_down(arr, smallest-1, 'min')


bubble_down(test_arr, 0, 'min')
print(f'Bubble Down completed. Output: {test_arr}')