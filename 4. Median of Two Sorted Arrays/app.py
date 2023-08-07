''' 
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) ->float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Step 1. Merge the array
        # Step 2. Use quick sort to sort the new array
        # Step 3. Get the middle number
        #   - if the length is even number the median is two middle number sumed 
        #   - then dived by two
        #   - esle the middle is the the lenght dived by 2 rouded to the nearest whole number

        new_arry = nums1+nums2
        sorted_array = quicksort(new_arry)
        length = len(sorted_array)
        if length%2 == 0:
            return (sorted_array[(length//2)-1] + sorted_array[(length//2)])/2
        else:
            return sorted_array[(length//2)]




def quicksort(arr: list[int]):
    """
    quick sort algo to sort the marged array
    """
    if len(arr)<= 1:
        return arr

    pivot = arr[:-1][0]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


print(findMedianSortedArrays([1,3],[2]))