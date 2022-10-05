def divide(self, unsorted, lower, upper):
    """ recrusive function to divide array into 2 sub arrays for sorting """
    
    # recursive base case reached
    if upper <= lower:
        return
    
    # get middle element for split
    mid = (lower + upper) // 2
    
    # divide array at midpoints
    divide(unsorted, lower, mid)
    divide(unsorted, mid + 1, upper)
    
    # merge sorted arrays
    merge(unsorted, lower, mid, mid + 1, upper)

    
def merge(unsorted, l_lower, l_upper, r_lower, r_upper):
    """ merging two sorted arrays to one sorted array """
    
    # extract left and right indices
    i, j = l_lower, r_lower
    
    # initialise temporary array
    temp = []
    
    # move through indices
    while i <= l_upper and j <= r_upper:
        
        # determine which value to put in temp next
        if unsorted[i].value <= unsorted[j].value:
            temp.append(unsorted[i])
            i += 1
        else:
            temp.append(unsorted[j])
            j += 1
    
    # one of the above conditions finishes first
    # therefore, handle the unfinished case
    while i <= l_upper:
        temp.append(unsorted[i])
        i += 1
    while j <= r_upper:
        temp.append(unsorted[j])
        j += 1
    
    # assign elements from temp array 
    for y, k in enumerate(range(l_lower, r_upper + 1)):
        unsorted[k] = temp[y]
