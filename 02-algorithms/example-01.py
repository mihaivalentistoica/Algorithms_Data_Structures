def bubble_sort(l):
    while True:
        swapped_values = False
        for i in range(1, len(l)):
            if l[i] < l[i - 1]:
                temp = l[i]
                l[i] = l[i - 1]
                l[i - 1] = temp
                swapped_values = True
        if not swapped_values:
            break  # List is sorted!


l = [5, 3, 7, 1, 4, 4, 2, 10]
bubble_sort(l)
print(f"Sorted list: {l}")
