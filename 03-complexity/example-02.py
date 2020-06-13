from timer import time_execution


@time_execution
def naive_minimum(l):
    if len(l) == 0:
        return None
    minimum = float("inf")
    for elem in l:
        if elem < minimum:
            minimum = elem
    return minimum


if __name__ == "__main__":
    for elements in [100_000, 1_000_000, 10_000_000]:
        print(f"For {elements} elements: ", end="")
        naive_minimum(range(elements))
