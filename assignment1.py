# Name: William Clements
# OSU Email: clemenwi@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 1
# Due Date:10/23/2023
# Description: 10 functions to operate on a static array


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple[int, int]:
    """receives a one-dimensional array of integers and returns a Python
    tuple with two values - the minimum and maximum values of the input array
            """

    max_value = min_value = arr.get(0)

    for index in range(1, arr.length()):
        current_value = arr.get(index)
        if current_value > max_value:
            max_value = current_value

        if current_value < min_value:
            min_value = current_value

    return (min_value, max_value)

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
            Function takes a static array as a parameter and returns the original array
                    with the following modifications:
                    --if the element in the original array is divisible by 3,
                    then the corresponding element in the new array will be the string 'fizz'.
                    --if the element in the original array is divisible by 5,
                    then the corresponding element in the new array will be the string 'buzz'.
                    --if the element in the original array is divisible by both 5 and 3,
                    then the corresponding element in the new array will be the string 'fizzbuzz'.
                    --if the element in the original array is neither divisible by 3 nor 5,
                    then the corresponding element in the new array will remain the same as in the
                    original array."""

    length = arr.length()
    new_arr = StaticArray(length)

    for index in range(0, length):
        new_arr.set(index, arr.get(index))

    for index in range(0, arr.length()):
        if arr.get(index) % 3 == 0 and arr.get(index) % 5 != 0:
            new_arr.set(index, "fizz")

        elif arr.get(index) % 5 == 0 and arr.get(index) % 3 != 0:
            new_arr.set(index, "buzz")

        elif arr.get(index) % 5 == 0 and arr.get(index) % 3 == 0:
            new_arr.set(index, "fizzbuzz")

    return new_arr

# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """Reverses the order of elements in the StaticArray in place"""
    length = arr.length()

    for index in range(length // 2):  # Loop through half of the array
        opposite_index = length - index - 1  # Calculate the index of the opposite element
        temp = arr.get(index)  # Temporary variable to store the current element
        arr.set(index, arr.get(opposite_index))  # Swap elements
        arr.set(opposite_index, temp)


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """receives two parameters - a StaticArray and an integer value called
                'steps'. The function will create and return a new StaticArray, which contains all the
                elements from the original array, but their position has shifted right or left steps number of
                times, without modifying the original array. If steps is a positive integer,
                the elements will be rotated to the right. If steps is a negative
                integer, they will rotate to the left."""
    length = arr.length()
    new_array = StaticArray(length)  # Create a new StaticArray to store the rotated elements

    for index in range(length):
        new_array.set(index, 0)  # Initialize the new array with 0

    for index in range(length):
        temp = arr.get(index)
        new_index = (index + steps) % length  # Calculate the new index after rotation

        new_array.set(new_index, temp)

    return new_array  # Return the rotated array

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """Receives the two integers start and end, and returns a StaticArray that contains all the
    consecutive integers between start and end(inclusive)."""

    current_value = start

    end_value = end

    length = abs(
        end_value - current_value) + 1  # we add 1 to the length of the array to account for the array range being inclusive

    new_array = StaticArray(
        length)  # creates an array of the appropriate length, given the range between its start and endpoints

    for index in range(length):  # loop keeps placing items into the new_array, starting with the current_value, and
        # incrementing by 1
        new_array.set(index, current_value)

        if start < end:  # handles the case of an ascending array
            current_value += 1
        if start > end:  # handles the case of a descending array
            current_value -= 1

    return new_array  # returns an array containing the range of values specified by the 'start' and 'end' parameters

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """Method receives a StaticArray and returns an integer that describes whether the array is sorted.
                    Returns:
                        ● 1 if the array is sorted in strictly ascending order.
                        ● -1 if the list is sorted in strictly descending order.
                        ● 0 otherwise."""
    length = arr.length()

    if length <= 1:
        return 1  # An array with 0 or 1 element is considered sorted

    # Check for strictly ascending order
    if arr.get(0) < arr.get(1):
        for index in range(1, length - 1):
            if arr.get(index) >= arr.get(index + 1):
                return 0  # Not sorted

        return 1  # Strictly ascending

    # Check for strictly descending order
    elif arr.get(0) > arr.get(1):
        for index in range(1, length - 1):
            if arr.get(index) <= arr.get(index + 1):
                return 0  # Not sorted

        return -1  # Strictly descending

    return 0  # None of the above cases, not sorted

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple[object, int]:
    length = arr.length()

    max_frequency = 0
    mode_element = None

    def get_frequency_of_item(index: int):
        frequency = 1  # Start with 1 since the item itself has appeared once
        while index < length - 1 and arr.get(index) == arr.get(index + 1):
            frequency += 1
            index += 1
        return frequency

    index = 0
    while index < length:
        current_frequency = get_frequency_of_item(index)
        if current_frequency > max_frequency:
            max_frequency = current_frequency
            mode_element = arr.get(index)
        index += current_frequency  # Skip to the next distinct element

    return mode_element, max_frequency

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """Receives a StaticArray that is already in sorted order and returns a new StaticArray with duplicate values removed."""

    length = arr.length()

    # Initialize a new StaticArray to store non-duplicate values
    new_array = StaticArray(length)
    new_length = 0

    index = 0
    while index < length:
        current_element = arr.get(index)
        new_array.set(new_length, current_element)
        new_length += 1

        # Skip all duplicate occurrences
        while index < length - 1 and arr.get(index) == arr.get(index + 1):
            index += 1

        index += 1

    # Create a new StaticArray with the non-duplicate elements
    result_array = StaticArray(new_length)
    for i in range(new_length):
        result_array.set(i, new_array.get(i))

    return result_array

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """Receives a StaticArray and returns a new StaticArray with the content sorted in non-ascending order."""

    # Find the maximum and minimum values in the original array
    max_value = arr.get(0)
    min_value = arr.get(0)

    for index in range(1, arr.length()):
        item = arr.get(index)
        if item > max_value:
            max_value = item
        if item < min_value:
            min_value = item

    # Create an array to count the occurrences of each value
    count_array = [0] * (max_value - min_value + 1)
    for index in range(arr.length()):
        item = arr.get(index)
        count_array[item - min_value] += 1

    # Create the sorted array
    sorted_array = StaticArray(arr.length())
    sorted_index = 0

    for value in range(max_value, min_value - 1, -1):
        count = count_array[value - min_value]
        for _ in range(count):
            sorted_array.set(sorted_index, value)
            sorted_index += 1

    return sorted_array

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """Receives a StaticArray where the elements are in sorted order and returns a new StaticArray with squares of the values from the original array, sorted in non-descending order. The original array must not be modified."""


