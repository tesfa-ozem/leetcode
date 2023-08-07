'''
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2. Please note that your returned answers (both index1 and index2)
are not zero-based.
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

def two_sum(target, numbers)->(int,int):
	# Constaints:
	# 1. index1 < index 2
	# 2. index1 == 0 and index2==0
	# 3. index1 + index2 = target
	# Loop through the list of numbers
	# create another loop for the index2;
	#  This should start at the next index after index 1
	# For the first loop start from index zero and end at len -1
	# for the the second loop start at index1+1 till end

	for i in range(0,len(numbers)-1):
		for x in range(i+1,len(numbers)):
			print(i,x)
			if numbers[i] < numbers[x] and numbers[i] >0 and numbers[x] > 0:
				result = numbers[i]+numbers[x]
				if result == target:
					return (i,x)

	return (0,0)

def two_sum_map(target, numbers):
	# subtract the first element with the taret.
	# store the result in list
	# check if the nth item in the list equals the nth+1 index of the numbers
	store = []
	for i in range(1,len(numbers)):
		result = target - numbers[i-1]
		store.append(result)
		print(numbers[i],store[-1])
		if numbers[i] == store[-1]:
			return (i-1,i)
	return (0,0)



numbers=[2, 7, 11, 15] 
target=9

print(two_sum_map(target, numbers))