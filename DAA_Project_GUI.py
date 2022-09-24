import random
import time
import DAA_Project as dp # import the sorting functions file
from tkinter import*
import matplotlib.pyplot as plt

saved_input_size = 0
difference_running_bubble = 0
difference_running_selection = 0
difference_running_insertion = 0
difference_running_quicksort = 0
difference_running_quicksort3median = 0
difference_running_mergesort = 0
difference_running_heapsort = 0

numbers_list = []
gui_window = Tk()
# set size of the window
gui_window.geometry("800x700")
# title of the window
gui_window.title("Sorting Algorithms")
# create text label for the textbox
written_text = Label(gui_window, text="Enter the input size (greater than 0)", font=('Helvatical bold' ,20))
written_text.place(x= 30, y=30)
# create textbox
textbox = Text(gui_window, width=10, height=2, font=('Helvatical bold' ,20))
textbox.place(x=400, y=20)

bubble_sort_execution_label = Label(gui_window, text='')
bubble_sort_execution_label.place(x= 200, y= 150)

selection_sort_execution_label = Label(gui_window, text='')
selection_sort_execution_label.place(x= 200, y= 200)

insertion_sort_execution_label = Label(gui_window, text='')
insertion_sort_execution_label.place(x= 200, y= 250)

quick_sort_execution_label = Label(gui_window, text='')
quick_sort_execution_label.place(x= 200, y= 300)

quick_sort3median_execution_label = Label(gui_window, text='')
quick_sort3median_execution_label.place(x= 200, y= 350)

merge_sort_execution_label = Label(gui_window, text='')
merge_sort_execution_label.place(x= 200, y= 400)

heap_sort_execution_label = Label(gui_window, text='')
heap_sort_execution_label.place(x= 200, y= 450)

def bubble_sort_algorithm_call():
    start_time = time.time()
    bubbleSortList = dp.bubble_sort(get_textbox_value())
    stop_time = time.time()
    global difference_running_bubble
    difference_running_bubble = stop_time - start_time
    running_time_bubble = "Execution time = " + f'{difference_running_bubble:.10f} seconds'
    bubble_sort_execution_label.configure(text=running_time_bubble)
    # print bubble sort list and execution time
    print("\nBubble Sort:", bubbleSortList, ",", "Running time:", f'{difference_running_bubble:.10f} seconds')

def selection_sort_algorithm_call():
    start_time = time.time()
    selectionSortList = dp.selection_sort(get_textbox_value())
    stop_time = time.time()
    global difference_running_selection
    difference_running_selection = stop_time - start_time
    running_time_selection = "Execution time = " + f'{difference_running_selection:.10f} seconds'
    selection_sort_execution_label.configure(text=running_time_selection)
    # print selection sort list and execution time
    print("\nSelection Sort:", selectionSortList, ",", "Running time:", f'{difference_running_selection:.10f} seconds')

def insertion_sort_algorithm_call():
    start_time = time.time()
    insertionSortList = dp.insertion_sort(get_textbox_value())
    stop_time = time.time()
    global difference_running_insertion
    difference_running_insertion = stop_time - start_time
    running_time_insertion = "Execution time = " + f'{difference_running_insertion:.10f} seconds'
    insertion_sort_execution_label.configure(text=running_time_insertion)
    # print insertion sort list and execution time
    print("\nInsertion Sort:", insertionSortList, ",", "Running time:", f'{difference_running_insertion:.10f} seconds')

def quick_sort_algorithm_call():
    start_time = time.time()
    quickSortList = dp.quick_sort(get_textbox_value())
    stop_time = time.time()
    global difference_running_quicksort
    difference_running_quicksort = stop_time - start_time
    running_time_quicksort = "Execution time = " + f'{difference_running_quicksort:.10f} seconds'
    quick_sort_execution_label.configure(text=running_time_quicksort)
    # print quick sort list and execution time
    print("\nQuick Sort:", quickSortList, ",", "Running time:", f'{difference_running_quicksort:.10f} seconds')

def quick_sort_algorithm_3median_call():
    start_time = time.time()
    quickSort3medianList = dp.quick_sort_3Median(get_textbox_value())
    stop_time = time.time()
    global difference_running_quicksort3median
    difference_running_quicksort3median = stop_time - start_time
    running_time_quicksort_3median = "Execution time = " + f'{difference_running_quicksort3median:.10f} seconds'
    quick_sort3median_execution_label.configure(text=running_time_quicksort_3median)
    # print quick sort 3 median list and execution time
    print("\nQuick Sort 3 median:", quickSort3medianList, ",", "Running time:", f'{difference_running_quicksort3median:.10f} seconds')

def merge_sort_algorithm_call():
    start_time = time.time()
    mergeSortList = dp.merge_sort(get_textbox_value())
    stop_time = time.time()
    global difference_running_mergesort
    difference_running_mergesort = stop_time - start_time
    running_time_mergesort = "Execution time = " + f'{difference_running_mergesort:.10f} seconds'
    merge_sort_execution_label.configure(text=running_time_mergesort)
    # print merge sort list and execution time
    print("\nMerge Sort:", mergeSortList, ",", "Running time:", f'{difference_running_mergesort:.10f} seconds')

def heap_sort_algorithm_call():
    start_time = time.time()
    heapSortList = dp.heap_sort(get_textbox_value())
    stop_time = time.time()
    global difference_running_heapsort
    difference_running_heapsort = stop_time - start_time
    running_time_heapsort = "Execution time = " + f'{difference_running_heapsort:.10f} seconds'
    heap_sort_execution_label.configure(text=running_time_heapsort)
    # print heap sort list and execution time
    print("\nHeap Sort:", heapSortList, ",", "Running time:", f'{difference_running_heapsort:.10f} seconds')

def graph_plot():
    global difference_running_bubble
    global difference_running_selection
    global difference_running_insertion
    global difference_running_quicksort
    global difference_running_quicksort3median
    global difference_running_mergesort
    global difference_running_heapsort
    execution_values = [round(difference_running_quicksort3median, 5), round(difference_running_quicksort, 5), round(difference_running_mergesort, 5), round(difference_running_heapsort, 5), round(difference_running_insertion, 5), round(difference_running_selection, 5), round(difference_running_bubble, 5)]
    sorting_names = ["Quick3med", "Quick", "Merge", "Heap", "Insertion", "Selection", "Bubble"]
    plt.ylabel("Time in seconds")
    plt.xlabel("Sorting algorithms")
    plt.bar(sorting_names, execution_values)
    # print each value on the histogram chart
    for each_value in range(len(sorting_names)):
        plt.text(each_value, execution_values[each_value], execution_values[each_value], va="bottom", ha="center", fontsize='x-small')
    plt.show()

def line_plot():
    global difference_running_bubble
    global difference_running_selection
    global difference_running_insertion
    global difference_running_quicksort
    global difference_running_quicksort3median
    global difference_running_mergesort
    global difference_running_heapsort
    execution_values = [round(difference_running_quicksort3median, 5), round(difference_running_quicksort, 5), round(difference_running_mergesort, 5), round(difference_running_heapsort, 5), round(difference_running_insertion, 5), round(difference_running_selection, 5), round(difference_running_bubble, 5)]
    sorting_names = ["Quick3med", "Quick", "Merge", "Heap", "Insertion", "Selection", "Bubble"]
    plt.ylabel("Time in seconds")
    plt.xlabel("Sorting algorithms")
    plt.plot(sorting_names, execution_values)
    # print each value on the line chart
    for each_value in range(len(sorting_names)):
        plt.text(each_value, execution_values[each_value], execution_values[each_value], fontsize='x-small', ha="center", va="bottom")
    plt.show()


# create bubble sort button
bubble_sort_button = Button(text="Bubble Sort", command=lambda: [bubble_sort_algorithm_call()])
bubble_sort_button.place(x=25, y=150)

# create selection sort button
selection_sort_button = Button(text="Selection Sort", command=lambda: [selection_sort_algorithm_call()])
selection_sort_button.place(x=25, y=200)

# create insertion sort button
insertion_sort_button = Button(text="Insertion Sort", command=lambda: [insertion_sort_algorithm_call()])
insertion_sort_button.place(x=25, y=250)

# create quick sort button
quick_sort_button = Button(text="Quick Sort", command=lambda: [quick_sort_algorithm_call()])
quick_sort_button.place(x=25, y=300)

# create quick sort 3 median button
quick_sort_3medianbutton = Button(text="Quick 3 median", command=lambda: [quick_sort_algorithm_3median_call()])
quick_sort_3medianbutton.place(x=25, y=350)

# create merge sort button
merge_sort_button = Button(text="Merge Sort", command=lambda: [merge_sort_algorithm_call()])
merge_sort_button.place(x=25, y=400)

# create heap sort button
heap_sort_button = Button(text="Heap Sort", command=lambda: [heap_sort_algorithm_call()])
heap_sort_button.place(x=25, y=450)

# create graph button
graph_button = Button(text="Histogram graph", command=lambda: [graph_plot()])
graph_button.place(x=200, y=600)

# create line graph button
line_graph_button = Button(text="Line chart", command=lambda: [line_plot()])
line_graph_button.place(x=500, y=600)

def get_textbox_value():
    get_input_text = textbox.get("1.0", "end-1c")
    global saved_input_size
    global numbers_list
    if saved_input_size != get_input_text:
        saved_input_size = get_input_text
        numbers_list = random.sample(range(0, int(get_input_text)), int(get_input_text))
    return numbers_list

gui_window.mainloop()