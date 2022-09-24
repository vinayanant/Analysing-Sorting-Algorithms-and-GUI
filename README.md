# Analysing-Sorting-Algorithms-and-GUI
Built a convenient user interface using Tkinter and Python to view the comparison of execution times and functionality of 7 different types of sorting algorithms. Implemented histogram and line chart to show the results using Matplotlib. Handles data size over a million.

Programming language used - Python
Version: Python 3.8.8

How to run the code - Steps are mentioned below:

Steps to execute code using terminal:
1. Make sure that Python 3.8.8 is installed on the system
2. Open terminal and check the python version by using command "python --version"
3. Navigate to the location of the folder where the files are located through the terminal using command "cd <folderpath>"
4. Type command "ls" to see the list of files
5. Type command "python "filename".py" and press enter
6. Enter the input size greater than 0
7. Result will appear which shows the list to sort along with sorted list for all the sorting algorithms with their execution time in seconds

Steps to execute GUI using terminal:
1. Follow the same above steps from 1 to 5
2. A new GUI window will appear
3. Enter the input size greater than 0
4. Click on respective buttons to see their execution time in seconds(Ex: click on Bubble sort button to see the execution time for bubble sort algorithm). While execution the result will also appear in the terminal or console(if using Pycharm IDE)
5. Click on "Histogram graph" or "Line chart" button to see their difference in running times

Notes:
This code is successfully tested on MacBook terminal and PyCharm 2021.3.3 (Community Edition)

Tested Output:
An example of the tested execution on terminal is as follows:

(base) vinay@Vinays-MacBook-Air project % python daa_project.py

Enter the input size: 10

List to sort: [2, 4, 7, 0, 5, 8, 6, 3, 1, 9]

Bubble Sort: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] , Running time: 0.0000598431 seconds

Selection Sort: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] , Running time: 0.0000407696 seconds

Insertion Sort: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] , Running time: 0.0000250340 seconds

Merge Sort: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] , Running time: 0.0001368523 seconds

Quick Sort: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] , Running time: 0.0000522137 seconds

Quick Sort 3 median: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] , Running time: 0.0000438690 seconds

Heap Sort: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] , Running time: 0.0001730919 seconds
