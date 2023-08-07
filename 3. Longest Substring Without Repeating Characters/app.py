def lengthOfLongestSubstring(s: str) -> int:
    # Constraints
    # longest substring without repeating
    # The substring should not innclude duplicate characters
    # count characters from a starting point till a duplicate appears
    # update the starting point to be the duplicate
    # what happens when you encounter another duplicate from beyond the starting point
    # check if the index of the duplicate is less than the starting point.
    # this means the dulicate is behind the starting point
    # start counting again from the duplicate repating the above 
    # compare the length and store the 

    start_point, max_length, store = 0, 0, {}
    for i,c in enumerate(s):
        if c in store and start_point <= store[c]:
            
            start_point = store[c] + 1
        else:
            max_length = max(i-start_point+1,max_length)
        store[c] = i

    return max_length

s = 'bbbbbsv'
print(lengthOfLongestSubstring(s=s))
