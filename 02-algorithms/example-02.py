def insertion_sort(l):
    for i in range(1, len(l)):
        current = l[i]
        j = i - 1
        while j >= 0 and l[j] > current:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = current


l = [5, 3, 7, 1, 4, 4, 2, 10]
insertion_sort(l)
print(f"Sorted list: {l}")
