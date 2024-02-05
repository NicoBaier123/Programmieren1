import timeit # import timeit module


array = [1, 3, 2, 5, 4, 8, 7, 6, 10, 9, 5, 3, 2, 1]

def bubble_sort(arr): 
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def timsort_sort(arr):
    return sorted(arr)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr


# Measure time for Bubble Sort
bubble_sort_time = timeit.timeit(lambda: bubble_sort(array.copy()), number=10000)

# Measure time for Timsort (using sorted function)
timsort_time = timeit.timeit(lambda: timsort_sort(array.copy()), number=10000)

# Measure time for Timsort (using sorted function)
quicksort_time = timeit.timeit(lambda: quick_sort(array.copy()), number=10000)

# Measure time for Timsort (using sorted function)
insertionsort_time = timeit.timeit(lambda: insertion_sort(array.copy()), number=10000)

# Measure time for Timsort (using sorted function)
selectionsort_time = timeit.timeit(lambda: selection_sort(array.copy()), number=10000)

print(f"Bubble Sort Time: {bubble_sort_time} seconds")
print(f"Timsort Time: {timsort_time} seconds")
print(f"Quick Sort Time: {quicksort_time} seconds")
print(f"Insertionsort Time: {insertionsort_time} seconds")
print(f"Selection Sort Time: {selectionsort_time} seconds")


