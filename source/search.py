#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    #TODO: implement linear search recursively here
    
    #BASE CASES

    #first item is wanted item
    if array[index] == item:     # base case - first index is key
        return 0

    #only one item in list and item is not wanted item
    if len(array) == 1 and array[0] != item:
        return None

    
    #as long as index not out of list range
    while index < len(array)-1:

        #if that position of the array contains wanted item
        if array[index] == item:
            #return the index at which it found it
            return index

        #check if the index of the array contains item
        if array[index] != item:

            #if it doesn't increment the index by 1
            index += 1

            print(index)
            #call the function again
            return linear_search_recursive(array, item, index)
        
    #item not in list
    return None 

    

    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
        start = 0
        end = len(array)-1
        match = False

        while start<=end and not match:
            middle = (start + end)//2
            if array[middle] == item:
                match = True
                return middle
            else:
                if item < array[middle]:
                    end = middle-1
                else:
                    start = middle+1
        return None

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    #TODO: implement binary search recursively here
    #BASE CASES

    #doesn't search through list if first item is item inputted
    if array[0] == item:
        return 0

    #can only return one item if length of list is 1
    if len(array) == 1 and array[0] != item:
        return None

    match = False
    middle = (len(array)//2)
    left_half = array[:middle]
    right_half = array[middle:]

    if left_half[0] != item and len(left_half) != 0:
        return binary_search_recursive(left_half, item, left=None, right=None)
    if right_half[0] != item and len(right_half) != 0:
        return binary_search_recursive(right_half, item, left=None, right=None)
    if right_half[0] == item:
        match = True
        return [item]
    if left_half[0] == item:
        match = True
        return [item]
    
    return None

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
