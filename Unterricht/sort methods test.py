import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def test_sorting_methods():
    array_size = 10000
    random_array = generate_random_array(array_size)

    start_time = time.time()
    bubble_sort(random_array.copy())
    bubble_sort_time = time.time() - start_time

    start_time = time.time()
    selection_sort(random_array.copy())
    selection_sort_time = time.time() - start_time

    start_time = time.time()
    insertion_sort(random_array.copy())
    insertion_sort_time = time.time() - start_time

    start_time = time.time()
    merge_sort(random_array.copy())
    merge_sort_time = time.time() - start_time

    start_time = time.time()
    quick_sort(random_array.copy(), 0, len(random_array) - 1)
    quick_sort_time = time.time() - start_time

    start_time = time.time()
    sorted(random_array.copy())
    sorted_time = time.time() - start_time

    print(f"Bubble Sort Time: {bubble_sort_time} seconds")
    print(f"Selection Sort Time: {selection_sort_time} seconds")
    print(f"Insertion Sort Time: {insertion_sort_time} seconds")
    print(f"Merge Sort Time: {merge_sort_time} seconds")
    print(f"Quick Sort Time: {quick_sort_time} seconds")
    print(f"Sorted Time: {sorted_time} seconds")

test_sorting_methods()
