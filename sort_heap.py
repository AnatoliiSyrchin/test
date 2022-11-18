def heap_sort(arr):
    len_arr = len(arr)
    max_heap(arr)
    for length in range(len_arr - 1, 0, -1):
        arr[0], arr[length] = arr[length], arr[0]
        print(length, arr)
        heapify(arr, 0, length)


def max_heap(arr):
    len_arr = len(arr)
    for el_idx in range(len_arr - 1, 0, -1):
        parent = (el_idx - 1) // 2
        heapify(arr, parent, len_arr)


def heapify(arr, idx, arr_len):
    l_child_idx = 2 * idx + 1
    r_child_idx = 2 * idx + 2
    largest = idx

    if l_child_idx < arr_len and arr[l_child_idx] > arr[idx]:
        largest = l_child_idx

    if r_child_idx < arr_len and arr[r_child_idx] > arr[largest]:
        largest = r_child_idx
    
    if largest != idx:
        arr[largest], arr[idx] = arr[idx], arr[largest]
        heapify(arr, largest, arr_len) 


if __name__ == '__main__':
    arr = [ 7, 4, 10, 5, 6]
    max_heap(arr)
    heap_sort(arr)
    print('result', arr)

