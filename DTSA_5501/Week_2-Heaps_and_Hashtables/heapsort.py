from heapify import heapify
from heap_delete import heap_delete

def heap_sort(arr):
  heapify(arr, 'min')
  result = []
  for i in range(len(arr)):
    result.append(arr[0])
    heap_delete(arr, 1, 'min')
  return result


outp = heap_sort([-5, 24, -38, 3, 45, -16, 11, -49, 28, -13, 7, 39, -21, 16, -2, 34, -32, 20, -7, 42])
print(outp)