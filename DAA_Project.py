import random
import time

# Bubble sort: Swapping the adjacent elements repeatedly if they are in incorrect order
# bubble sort implementation function
def bubble_sort(numbers):
    # copying the random numbers generate to a new list
    bubble_sort_list = []
    bubble_sort_list.extend(numbers)
    # for loop to iterate over all the elements
    for each_iteration in range(len(bubble_sort_list)):
     # for loop that points to the element for comparison
     for each_index in range(len(bubble_sort_list)-(each_iteration+1)):
         # comparison of current element value with the next element value
         if bubble_sort_list[each_index] > bubble_sort_list[each_index+1]:
             # swap the two values
             bubble_sort_list[each_index], bubble_sort_list[each_index+1] = bubble_sort_list[each_index+1], bubble_sort_list[each_index]
    # return the final list
    return bubble_sort_list

# Selection sort: Finding the smallest element repeatedly from an unsorted set of elements and putting it at the beginning
# selection sort implementation function
def selection_sort(numbers):
    # copying the random numbers generate to a new list
    selection_sort_list = []
    selection_sort_list.extend(numbers)
    # for loop to iterate over all the elements
    for i in range(len(selection_sort_list)):
        # assign current element as the minimum value
        minimum_value = i
        # for loop to go over all elements and find minimum element possible
        for j in range(i+1, len(selection_sort_list)):
            # compare the element
            if selection_sort_list[j] < selection_sort_list[minimum_value]:
                # update the minimum value
                minimum_value = j
        # swap the elements
        selection_sort_list[minimum_value], selection_sort_list[i] = selection_sort_list[i], selection_sort_list[minimum_value]
    # return the final list
    return selection_sort_list

def insertion_sort(numbers):
    insertion_sort_list = []
    insertion_sort_list.extend(numbers)
    for i in range(1, len(insertion_sort_list)):
        key = insertion_sort_list[i]
        j = i - 1
        while j >= 0 and key < insertion_sort_list[j]:
            insertion_sort_list[j+1] = insertion_sort_list[j]
            j = j - 1
        insertion_sort_list[j+1] = key
    return insertion_sort_list


def merge(arr_a, arr_b):
    arr_c = []
    while arr_a and arr_b:
        if arr_a[0] > arr_b[0]:
            arr_c.append(arr_b[0])
            arr_b.pop(0)
        else:
            arr_c.append(arr_a[0])
            arr_a.pop(0)
    while arr_a:
        arr_c.append(arr_a[0])
        arr_a.pop(0)
    while arr_b:
        arr_c.append(arr_b[0])
        arr_b.pop(0)
    return arr_c

def merge_sort(arr_a):
    list_to_sort = []
    list_to_sort.extend(arr_a)
    list_length = len(list_to_sort)
    if list_length == 1:
        return list_to_sort
    half_of_length = list_length // 2
    list1 = list_to_sort[:half_of_length]
    list2 = list_to_sort[half_of_length:]
    # print("List 1:", list1)
    # print("List 2:", list2)
    list1 = merge_sort(list1)
    list2 = merge_sort(list2)
    return merge(list1, list2)

def quickSort1(quick_sort_list, low_index, high_index, is3Median = 0):
    if low_index < high_index:
        if is3Median == 0:
            partition_index = partition(quick_sort_list, low_index, high_index)
        elif is3Median == 1:
            partition_index = qs3MedianPartition(quick_sort_list, low_index, high_index)
        quickSort1(quick_sort_list, low_index, partition_index-1)
        quickSort1(quick_sort_list, partition_index+1, high_index)

def partition(quick_sort_list, low_index, high_index):
    quick_sort_pivot = quick_sort_list[high_index]
    i = low_index -1
    for j in range(low_index,high_index):
        if quick_sort_list[j] < quick_sort_pivot:
            i = i+1
            quick_sort_list[i],quick_sort_list[j] = quick_sort_list[j],quick_sort_list[i]
    quick_sort_list[i+1], quick_sort_list[high_index] = quick_sort_list[high_index], quick_sort_list[i+1]
    return i+1

def qs3MedianPartition(quick_sort_list, low_index, high_index):
    # Find the median index
    medianIndex = (low_index + high_index)//2
    if quick_sort_list[high_index] < quick_sort_list[low_index]:
        quick_sort_list[high_index], quick_sort_list[low_index] = quick_sort_list[low_index], quick_sort_list[high_index]
    if quick_sort_list[high_index] < quick_sort_list[medianIndex]:
        quick_sort_list[high_index], quick_sort_list[medianIndex] = quick_sort_list[medianIndex], quick_sort_list[high_index]
    if quick_sort_list[medianIndex] < quick_sort_list[low_index]:
        quick_sort_list[medianIndex], quick_sort_list[low_index] = quick_sort_list[low_index], quick_sort_list[medianIndex]

    quick_sort_list[medianIndex], quick_sort_list[high_index-1] = quick_sort_list[high_index-1], quick_sort_list[medianIndex]

    pivot = quick_sort_list[high_index-1]
    leftEntryPosition = low_index
    rightEntryPosition = high_index - 1
    while leftEntryPosition < rightEntryPosition:
        leftEntryPosition = leftEntryPosition + 1
        rightEntryPosition = rightEntryPosition - 1
        while quick_sort_list[leftEntryPosition] < pivot:
            leftEntryPosition = leftEntryPosition + 1
        while quick_sort_list[rightEntryPosition] > pivot:
            rightEntryPosition = rightEntryPosition - 1
        if leftEntryPosition >= rightEntryPosition:
            break
        else:
            quick_sort_list[leftEntryPosition], quick_sort_list[rightEntryPosition] = quick_sort_list[rightEntryPosition], quick_sort_list[leftEntryPosition]

    # Move pivot to it's correct position
    quick_sort_list[leftEntryPosition], quick_sort_list[high_index-1] = quick_sort_list[high_index-1], quick_sort_list[leftEntryPosition]
    return leftEntryPosition

def quick_sort(numbers):
    quick_sort_list = []
    quick_sort_list.extend(numbers)
    quickSort1(quick_sort_list, 0, len(quick_sort_list) - 1)
    return quick_sort_list

def quick_sort_3Median(numbers):
    quick_sort_list = []
    quick_sort_list.extend(numbers)
    MedianExecution = 1
    quickSort1(quick_sort_list, 0, len(quick_sort_list) - 1, MedianExecution)
    return quick_sort_list

# heap sort implementation function
def heap_sort(numbers):
    # copying the random numbers generated to a new list
    heap_sort_list = []
    heap_sort_list.extend(numbers)
    buildHeap(heap_sort_list)
    n = len(heap_sort_list)
    # Here the reducing value of i in for loop is for the reducing size of the heap
    for i in range(n-1, -1, -1):
        # The largest item is at the root(index 0) of the heap, replacing it with the last item of the heap (index i)
        heap_sort_list[0], heap_sort_list[i] = heap_sort_list[i], heap_sort_list[0]
        # n = n - 1
        heapify(heap_sort_list, i, 0)
    return heap_sort_list

def buildHeap(numbers):
    n = len(numbers)
    # Building a max heap from the input list of numbers
    for i in range(n//2 -1, -1, -1):
        heapify(numbers, n, i)

def heapify(numbers, n, i):
    left = 2 * i
    right = 2 * i + 1
    # n = len(numbers)
    if(left + 1 < n) and (numbers[left+1] > numbers[i]):
        max_value = left + 1
    else:
        max_value = i
    if (right+1 < n) and (numbers[right+1] > numbers[max_value]):
        max_value = right+1
    if(max_value != i):
        numbers[i], numbers[max_value] = numbers[max_value], numbers[i]
        heapify(numbers, n, max_value)

input_size = "1"
def main():
    # input from the user
    global input_size
    input_size = input("\nEnter the input size: ")
    numbers_list = random.sample(range(0, int(input_size)), int(input_size))

    print("\nList to sort:", numbers_list)
    # calculate start time for bubble sort
    start_time = time.time()
    bubbleSortList = bubble_sort(numbers_list)
    stop_time = time.time()
    running_time_bubble = stop_time - start_time
    # print bubble sort list and execution time
    print("\nBubble Sort:", bubbleSortList, ",", "Running time:", f'{running_time_bubble:.10f} seconds')

    # calculate start time for selection sort
    start_time = time.time()
    selectionSortList = selection_sort(numbers_list)
    stop_time = time.time()
    running_time_selection = stop_time - start_time
    # print selection sort list and execution time
    print("\nSelection Sort:", selectionSortList, ",", "Running time:", f'{running_time_selection:.10f} seconds')

    # calculate start time for insertion sort
    start_time = time.time()
    insertionSortList = insertion_sort(numbers_list)
    stop_time = time.time()
    running_time_insertion = stop_time - start_time
    # print insertion sort list and execution time
    print("\nInsertion Sort:", insertionSortList, ",", "Running time:", f'{running_time_insertion:.10f} seconds')

    # calculate start time for merge sort
    start_time = time.time()
    mergeSortList = merge_sort(numbers_list)
    stop_time = time.time()
    running_time_merge = stop_time - start_time
    # print merge sort list and execution time
    print("\nMerge Sort:", mergeSortList, ",", "Running time:", f'{running_time_merge:.10f} seconds')

    # calculate start time for quick sort
    start_time = time.time()
    quickSortList = quick_sort(numbers_list)
    stop_time = time.time()
    running_time_quick = stop_time - start_time
    # print quick sort list and execution time
    print("\nQuick Sort:", quickSortList, ",", "Running time:", f'{running_time_quick:.10f} seconds')

    # calculate start time for quick sort 3 median
    start_time = time.time()
    quickSort3medianList = quick_sort_3Median(numbers_list)
    stop_time = time.time()
    running_time_quick_3median = stop_time - start_time
    # print quick sort 3 median list and execution time
    print("\nQuick Sort 3 median:", quickSort3medianList, ",", "Running time:", f'{running_time_quick_3median:.10f} seconds')

    # calculate start time for heap sort
    start_time = time.time()
    heapSortList = heap_sort(numbers_list)
    stop_time = time.time()
    running_time_heap = stop_time - start_time
    # print heap sort list and execution time
    print("\nHeap Sort:", heapSortList, ",", "Running time:", f'{running_time_heap:.10f} seconds')


if __name__ == "__main__":
    main()




