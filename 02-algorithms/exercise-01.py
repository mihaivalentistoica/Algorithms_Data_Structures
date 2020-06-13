"""
1. Add loop counter to bubble sort example. Increment it for every loop this
   sort has to perform. At the end of the sorting procedure, print the number
   of loops it took to sort the array.
2. Think about best and worst cases of arrays to sort using bubble sort.
   - Is there a chance of sorting an array in 1 loop?
   Yes, if the array is already sorted.
   - How many loops does an array of length N need to be sorted, where Nth 
     element is the minimum?
   N
"""


def bubble_sort(l):
    loop_count = 0
    while True:
        loop_count += 1
        swapped_values = False
        for i in range(1, len(l)):
            if l[i] < l[i - 1]:
                temp = l[i]
                l[i] = l[i - 1]
                l[i - 1] = temp
                swapped_values = True
        if not swapped_values:
            print(f"It took {loop_count} loops to sort this list!")
            break  # List is sorted!


l = [5, 3, 7, 1, 4, 4, 2, 10]
bubble_sort(l)
print(f"Sorted list: {l}")
