#!/usr/bin/python3
import time


def insertionSortIterative(arr):
    index = 0
    while index < len(input_array):
        if index == len(input_array) - 1 or index == 0:
            pass
        else:
            current_number = input_array[index]
            previous_number = input_array[index - 1]

            if current_number < previous_number:
                input_array[index] = previous_number
                input_array[index - 1] = current_number
                base_index = index - 1  # now continue check to the front
                while base_index:
                    current_number = input_array[base_index]
                    previous_number = input_array[base_index - 1]
                    if current_number < previous_number:
                        input_array[base_index] = previous_number
                        input_array[base_index - 1] = current_number
                    base_index -= 1
        index += 1


print("Insertion Sort Iteratively")
input_array = [4, 6, 2, 3, 1, 8]
print(input_array)
start_time = time.time()
insertionSortIterative(input_array)
end_time = time.time()
print(input_array)
print(f"Iterative insertion sort took {(end_time-start_time)*1000}ms")


def insertionSortRecurse(arr):
    """
    Not necessarily a proper implementation as this recursively goes 
    to the beginning each time there is a swap instead of just 
    continually comparing to previous numbers.
    """
    index = 0
    while index < len(arr):
        if index == len(arr) - 1:
            break
        current_number = arr[index]
        next_number = arr[index + 1]
        if next_number < current_number:
            arr[index] = next_number
            arr[index + 1] = current_number
            insertionSortRecurse(arr)
        index += 1


print("\n\nInsertion Sort Recursively")
input_array = [8, 6, 2, 3, 1, 4]
print(input_array)
start_time = time.time()
insertionSortRecurse(input_array)
end_time = time.time()
print(input_array)
print(f"Recursive insertion sort took {(end_time-start_time)*1000}ms")
