# -*- coding: utf-8 -*-
"""Sorting Algorithm Visualizer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NDWT_iwaklqqvywvQPgK0PB9SMzhxMHJ

David Luu CIS 4100 Sorting Algorithm Visualizations
"""

# Import libraries
import time
import random
import matplotlib.pyplot as plt
import numpy as np

# Function to control the speed
speed = 1.0
def set_speed():

  # Creates a global variable that all functions have access to
  global speed

  # Checks user input, if valid input then change speed otherwise run at default speed
  try:
    user_speed = float(input("Enter speed (Greater than 0.0, Less than 1 for slower, Greater than 1 for faster, 1 for default): "))
    if user_speed > 0:
      speed = user_speed
    else:
      print("Speed must be greater than 0. Using default speed 1")
  except ValueError:
    print("Invalid speed. Using default speed 1")

# Function to create an array of random size and numbers
def random_array(size):
  # Generate a random array with integers between 1 and 1000
  return np.random.randint(1, 1000, size)

# Function to ask whether user wants to user their own array or the randomly generated one
def get_array():
  user_input = input("Do you want to use your own array? (y/n): ").lower()
  if user_input == "y":
    try:
      # Ask user for array details
      array_size = int(input("Enter the size of the array: "))
      array = []
      print(f"Enter {array_size} elements for the array: ")
      for i in range(array_size):
        while True:
          try:
            element = int(input(f"Element {i + 1}: "))
            array.append(element)
            break
          except ValueError:
            print("Please enter a valid integer.")
      return array
    except ValueError:
      print("Invalid size. Generating a random array.")
  # Fallback to randomly generated array
  else:
    try:
      random_size = int(input("Enter the size you want for the random array: "))
      return random_array(random_size)
    except ValueError:
      print("Invalid size. Generating a random array between sizes 25 and 50.")
      return random_array(random.randint(25, 50))

def sort_order():
  user_input = input("Do you want to sort in ascending or descending order? (asc/desc): ").lower()
  if user_input == 'desc':
    # False for descending order
    print("Sorting by descending order")
    return False
  # True for ascending order
  else:
    print("Sorting by ascending order")
    return True

# Function to print out each array separating each value with commas
def commas(array):
  print(", ".join(map(str, array)))

# Function to visualize the sorting algorithms
def visualize(array, title = "Sorting Process"):
  # Clears any previous plot
  plt.clf()
  plt.bar(range(len(array)), array, color = "blue")
  plt.title(title)
  plt.xlabel("Index")
  plt.ylabel("Value")
  # Pause to visualize the plot
  plt.pause(0.1)
  # Draw the updated plot
  plt.draw()

# Bubble sort function
def bubble_sort(array, ascending = True):
  # Start timer
  start_time_bub = time.time()

  # Determine the size of the array
  size = len(array)
  # Iterate the array and compare two values sending the larger one to the back until the array is sorted
  for i in range(size):
    for j in range(size - i - 1):
      if (array[j] > array[j + 1] and ascending) or (array[j] < array[j + 1] and not ascending):
        array[j], array[j + 1] = array[j + 1], array[j]

        # Speeds up or delays the time spent to run the function
        time.sleep(1.0 / speed)
  # End timer and calculate total runtime
  end_time_bub = time.time()
  runtime = end_time_bub - start_time_bub
  # Print runtime
  print(f"Bubble sort - Time elapsed: {runtime:.2f} seconds")
  commas(array)
  # Visualize the sorting process
  visualize(array, "Bubble Sort")
  return array



# Selection sort function
def selection_sort(array, ascending = True):
  #Start timer
  start_time_sel = time.time()

  # Determine the size of the array
  size = len(array)
  # Iterate the array and find the smallest element to bring to the front until the array is sorted
  for i in range(size):
    # Find the minimum element
    min_index = i
    for j in range(i + 1, size):
      if (array[j] < array[min_index] and ascending) or (array[j] > array[min_index] and not ascending):
        min_index = j
    # Swap the minimum element with the first element
    array[i], array[min_index] = array[min_index], array[i]

    # Speeds up or delays the time spent to run the function
    time.sleep(1.0 / speed)
  # End timer and calculate total runtime
  end_time_sel = time.time()
  runtime = end_time_sel - start_time_sel
  # Print runtime
  print(f"Selection sort - Time elapsed: {runtime:.2f} seconds")
  commas(array)
  # Visualize the sorting process
  visualize(array, "Selection Sort")
  return array



# Insertion sort function
def insertion_sort(array, ascending = True):
  #Start timer
  start_time_ins = time.time()

  # Determine the size of the array
  size = len(array)
  # Iterate the array starting from the second element and compare it to the first element, moving the larger element to the back until the array is sorted
  for i in range(1, size):
    # Current element
    key = array[i]
    j = i - 1
    # Move all the elements greater than the key, one to the left
    while j >= 0 and ((array[j] > key and ascending) or (array[j] < key and not ascending)):
      array[j + 1] = array[j]
      j -= 1
      # Speeds up or delays the time spent to run the function
      time.sleep(1.0 / speed)
    # Place the key after the last shifted element
    array[j + 1] = key

  # End timer and calculate total runtime
  end_time_ins = time.time()
  runtime = end_time_ins - start_time_ins
  # Print runtime
  print(f"Insertion sort - Time elapsed: {runtime:.2f} seconds")
  commas(array)
  # Visualize the sorting process
  visualize(array, "Insertion Sort")
  return array


def MERGED(array, ascending = True):
  #Start timer
  start_time_mrg = time.time()

  # Merge sort function
  def merge_sort(array, ascending = True):

    # Base case if the array has one or 0 elements then it is already sorted
    if len(array) <= 1:
      return array

    # Split the array into 3 parts, left, middle, and right
    mid = len(array) // 2
    left_half = merge_sort(array[:mid], ascending)
    right_half = merge_sort(array[mid:], ascending)

    # Merge the sorted halves
    merged_array = merge(left_half, right_half, ascending)

    return merged_array

  # Merge function to combine sorted halves
  def merge(left, right, ascending = True):
    # Create an empty array
    sorted_array = []
    i = j = 0

    # Compare the elements from both halves and append the smaller element to the sorted array
    while i < len(left) and j < len(right):
      if (left[i] < right[j] and ascending) or (left[i] > right[j] and not ascending):
        sorted_array.append(left[i])
        i += 1
      else:
        sorted_array.append(right[j])
        j += 1


      # Speeds up or delays the time spent to run the function
      time.sleep(1.0 / speed)

    # Append the remaining element
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

  final_array = merge_sort(array, ascending)
  # End and calculate total run time
  end_time_mrg = time.time()
  runtime = end_time_mrg - start_time_mrg
  # Print runtime
  print(f"Merge sort - Time elapsed: {runtime:.2f} seconds")
  commas(final_array)
  # Visualize the sorting process
  visualize(final_array, "Merge Sort")
  return final_array



# Quick sort function
def quick_sort(array, ascending = True):

  #Start timer
  start_time_qck = time.time()

  # Function to measure time and call the recursive quick sort
  def quick_recursive(array, low, high):
    if low < high:
      # Partition the array and get the pivot index
      pivot_index = partition(array, low, high, ascending)

      # Recursively sort elements before and after the pivot
      quick_recursive(array, low, pivot_index - 1)
      quick_recursive(array, pivot_index + 1, high)

  # Function to partition the array
  def partition(array, low, high, ascending):
    # Choosing the last element as the pivot
    pivot = array[high]
    # Pointer for the smaller element
    i = low - 1

    for j in range(low, high):
      if (array[j] < pivot and ascending) or (array[j] > pivot and not ascending):
        i += 1
        array[i], array[j] = array[j], array[i]

      # Speeds up or delays the time spent to run the function
      time.sleep(1.0 / speed)

    # Swap the pivot element with the element at i + 1
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

  # Call recursive function
  quick_recursive(array, 0, len(array) - 1)

  # End timer and calculate total runtime
  end_time_qck = time.time()
  runtime = end_time_qck - start_time_qck
  # Print runtime
  print(f"Quick sort - Time elapsed: {runtime:.2f} seconds")
  commas(array)  # Visualize the sorting process
  visualize(array, "Quick Sort")
  return array



# Heap sort function
def heap_sort(array, ascending = True):
  #Start timer
  start_time_hep = time.time()

  # Determine the size of the array
  size = len(array)
  # Start from the last non-leaf node and heapify each node by calling heapify function
  for i in range(size // 2 - 1, -1, -1):
    heapify(array, size, i, ascending)

  #Extract elements one by one from the heap
  for i in range(size - 1, 0, -1):
    # Swap the root (largest element) with the last element
    array[i], array[0] = array[0], array[i]

    # Heapify the reduced heap
    heapify(array, i, 0, ascending)

    # Speeds up or delays the time spent to run the function
    time.sleep(1.0 / speed)
  # End timer and calculate total runtime
  end_time_hep = time.time()
  runtime = end_time_hep - start_time_hep
  # Print runtime
  print(f"Heap sort - Time elapsed: {runtime:.2f} seconds")
  # Visualize the final sorted array
  visualize(array, title = "Heap Sort")
  commas(array)
  return array

# Heapify function to maintain the heap property
def heapify(array, size, root, ascending):
  largest = root
  # Left and right child
  left = 2 * root + 1
  right = 2* root + 2

  # Check if left child is larger than the root
  if left < size and ((array[left] > array[largest] and ascending) or (array[left] < array[largest] and not ascending)):
    largest = left
  # Check if right child is larger than current largest element
  if right < size and ((array[right] > array[largest] and ascending) or (array[right] < array[largest] and not ascending)):
    largest = right
  # If the largest is not the root then swap and continue heapifying
  if largest != root:
    array[root], array[largest] = array[largest], array[root]

    # Recursively heapify the affected subtree by calling itself
    heapify(array, size, largest, ascending)



def main():

  # Set speed of all sorting functions
  set_speed()

  # Assign an array to the variable
  array = get_array()

  # Get sorting order from user
  ascending = sort_order()

  # Perform different types of sorting to the array
  print("\nBubble Sort: ")
  bubble_sort(array.copy(), ascending)
  print("\nSelection Sort: ")
  selection_sort(array.copy(), ascending)
  print("\nInsertion Sort: ")
  insertion_sort(array.copy(), ascending)
  print("\nMerge Sort: ")
  MERGED(array.copy(),ascending)
  print("\nQuick Sort: ")
  quick_sort(array.copy(), ascending)
  print("\nHeap Sort: ")
  heap_sort(array.copy(), ascending)

main()