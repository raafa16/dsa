def bubble_sort(array):
    # We set swapped to True so the loop runs at least once
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                # Swap the elements
                array[i], array[i + 1] = array[i + 1], array[i]
                # Set the flag to True so we'll loop again
                swapped = True

    return array

# BigO(n)
