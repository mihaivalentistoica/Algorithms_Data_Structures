from timer import time_execution


@time_execution
def combine_all(l):
    result = []
    for i in range(len(l)):
        for j in range(len(l)):
            result.append((l[i], l[j]))
    return result


if __name__ == "__main__":
    for elements in [10, 100, 200, 400, 800]:
        print(f"For {elements} elements: ", end="")
        combine_all(range(elements))
