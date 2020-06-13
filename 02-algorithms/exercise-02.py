"""
1. Add element swap counter to insertion sort example. Increment it every time an element swaps place.
2. Think about best and worst cases of arrays to sort using insertion sort.
   - Is there a chance of sorting doing no insertions?
      Yes, for an already sorted list.
   - How many element swaps does a reversed array of length 10 need to be sorted?
      45
"""


def insertion_sort(l):
    swaps = 0
    for i in range(1, len(l)):
        current = l[i]
        j = i - 1
        while j >= 0 and l[j] > current:
            l[j + 1] = l[j]
            j -= 1
            swaps += 1
        l[j + 1] = current
    print(f"Performed {swaps} swaps")


l = [5, 3, 7, 1, 4, 4, 2, 10]
# To answer 2., uncomment
# l = list(reversed(range(10)))
insertion_sort(l)
print(f"Sorted list: {l}")
