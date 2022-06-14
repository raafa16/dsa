def selection_sort(array):
    for i in range(len(array)):
        # We assume that the first item of the unsorted segment is the smallest
        min_value = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_value]:
                min_value = j

        # Swap values of the lowest unsorted element with the first unsorted element
        array[i], array[min_value] = array[min_value], array[i]

    return array
