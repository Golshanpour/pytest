def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quick_sort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index-1)
        quick_sort(array, pivot_index+1, high)

#========================= for example ====================
        
my_array = [64, 34, 25, 12, 22, 11, 90, 5, -7, 11.2, -45.3, 111, 3, 444, -66]
quick_sort(my_array)
print("Sorted array:", my_array)

#==========================================================
