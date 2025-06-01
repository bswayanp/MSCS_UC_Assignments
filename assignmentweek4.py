import time
import random
import sys
sys.setrecursionlimit(10000)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def test_sorting_algorithms():
    sizes = [1000, 5000, 10000]
    for size in sizes:
        print(f"\nArray Size: {size}")
        for name, func in [("Quick Sort", quick_sort), ("Merge Sort", merge_sort)]:
            for data_type, data in [
                ("Sorted", list(range(size))),
                ("Reverse", list(range(size, 0, -1))),
                ("Random", [random.randint(1, size) for _ in range(size)])
            ]:
                start_time = time.perf_counter()
                func(data[:])
                end_time = time.perf_counter()
                print(f"{name} on {data_type} Data: {end_time - start_time:.6f} sec")

test_sorting_algorithms()
