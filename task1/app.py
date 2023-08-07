# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from typing import List

def solution(string):
    length = len(string)
    middle = length // 2
    result = ['']*length

    # String has an even number of characters
    if length % 2 == 0:
        for i in range(middle - 1, -1, -1):
            if string[i] != string[length - i - 1]:
                if string[i] == '?':
                    result[i] = string[length - i - 1]
                elif string[length - i - 1] == '?':
                    result[length - i - 1] = string[i]
                else:
                    return 'NO'

    else:  # String has an odd number of characters

        for i in range(middle - 1, -1, -1):
            if string[i] != string[length - i - 1]:
                if string[i] == '?':
                    result[i] = string[length - i - 1]
                elif string[length - i - 1] == '?':
                    result[length - i - 1] = string[i]
                else:
                    return 'NO'

    return ''.join(result)


def romanToInt(s: str) -> int:
    base =  {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    count = 0
    prev_val = 0

    for i in s[::-1]:
        curr_val = base[i]

        if curr_val >= prev_val:
            count += curr_val
        else:
            count -= curr_val

        prev_val = curr_val

    return count

def longestCommonPrefix(strs: list[str]) -> str:
        # iterate over the array 
        # check if the nth cha of each string is equal
        # create a set 
        # add the nth character of the strings to the set
        # compare the previous length  and current length of the set
        # if it increase by more than one roll back and print the prefix
        # edge case is if the next string is shorter
        # ["flower","flow","f"]
        # ["floower","floow","floo"]
        # if the nth index of any of the sring does not exist roll back
        # check if the nth index is less than the len of the string

        
        for x in range(len(strs[0])):
            print(x)
            for i in strs:
                if len(i) <= x or strs[0][x] != i[x]:
                    return strs[0][:x]
                # if i[count] not in pre_fix:
                #     
                
            # current_length = len(pre_fix)-current_length

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()  # Sort the input list
    seen = set()
    
    
    for i in range(len(nums)-2):
        # Skip duplicates of x
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, len(nums) - 1
        x = nums[i]
        target = -x

        while left < right:
            if (nums[left] + nums[right]) < target:
                left += 1
            elif (nums[left] + nums[right]) > target:
                right -= 1
            elif (nums[left] + nums[right]) == target:
                seen.add(tuple(sorted([x, nums[left], nums[right]])))
                left += 1
                right -= 1

    return [list(triplet) for triplet in seen]



def twoSum(numbers: list[int], target: int) -> list[int]:
        # Loop through the array
        # with two pointers start checking for the number
        # if the number we get is less than the target we icrease the pointer
        # if the number we get is higher we reduce the pointer 
        left, right = 0, len(numbers)-1
        result = []
        while left < right:
            print(left, right)
            if (numbers[left] + numbers[right]) < target:
                left += 1
            elif (numbers[left] + numbers[right]) > target:
                right -= 1
            elif (numbers[left] + numbers[right]) == target:
                result = [numbers[left], numbers[right]]
                break

        return result

def letterCombinations(digits: str) -> list[str]:
       # create a hashtable
       # get the arrays from the hash table and add them to a new array
       # loop through the array while shifting current and next pointers
        digit_map = {
           "2":"abc",          
           "3":"def",
           "4":"ghi",
           "5":"jkl",
           "6":"mno",
           "7":"pqrs",
           "8":"tuv",
           "9":"wxyz"
        } 
        new_array = []
        next_point = 1
        result = []

        if len(new_array) == 0:
            return new_array
        if len(new_array) == 1:
            return digit_map[digits]
        print(new_array)
        

    #     value = [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*B)] 
    # for A_row in new_array] 
        # for x in range(len(new_array)):
        #     for y in range(next_point,len(new_array)):
        #         if x == y and x != len(new_array):
        #             next_point += 1
        #         if x == y and x == len(new_array):
        #             next_point = 0
        #         print(new_array[x], new_array[y])
        return value

def solution(k: List[str]) -> List[str]:
    seen = k[0]
    
    for i in k[0]:
        for x in range(1, len(k)):
            if i not in k[x]:
                del seen[i]
                continue

    return seen


print(solution(["nellie", "leslie", "stella"]))
