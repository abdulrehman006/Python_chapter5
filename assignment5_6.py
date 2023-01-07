"""
(Bubble Sort) Sorting data (i.e. placing data into some particular order, such as
ascending or descending) is one of the most important computing applications. Python
lists provide a sort meth- od. In this exercise, readers implement their own sorting
function, using the bubble-sort method. In the bubble sort (or sinking sort), the smaller
values gradually “bubble” their way upward to the top of the list like air bubbles rising in
water, while the larger values sink to the bottom of the list. The pro- cess that compares
each adjacent pair of elements in a list in turn and swaps the elements if the second
element is less than the first element is called a pass. The technique makes several
passes through the list. On each pass, successive pairs of elements are compared. If a
pair is in increasing order, bubble sort leaves the values as they are. If a pair is in
decreasing order, their values are swapped in the list. After the first pass, the largest
value is guaranteed to sink to the highest index of a list. After the second pass, the
second largest value is guaranteed to sink to the second highest index of a list, and so
on. Write a program that uses the function bubbleSort to sort the items in a list.
"""


# Bubble sort in Python

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)
