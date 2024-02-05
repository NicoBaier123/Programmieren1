import sorting

def test_sorting():
    # Test case 1: Sorting an empty list should return an empty list
    assert sorting.bubble_sort([]) == []
    
    # Test case 2: Sorting a list with one element should return the same list
    assert sorting.bubble_sort([5]) == [5]
    
    # Test case 3: Sorting a list with multiple elements
    assert sorting.bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    
    # Test case 4: Sorting a list with duplicate elements
    assert sorting.bubble_sort([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    
    # Test case 5: Sorting a list with negative numbers
    assert sorting.bubble_sort([-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]) == [-9, -6, -5, -5, -5, -4, -3, -3, -2, -1, -1]
    
    # Test case 6: Sorting using timsort
    assert sorting.timsort_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    
    # Test case 7: Sorting using quicksort
    assert sorting.quick_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    
    # Test case 8: Sorting using insertion sort
    assert sorting.insertion_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    
    # Test case 9: Sorting using selection sort
    assert sorting.selection_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    
    print("All test cases passed!")

test_sorting()