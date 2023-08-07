from typing import List

def canJump(nums:List[int])-> bool:
	n = len(nums)
	dp = [False] * n
	dp[0] = True


	for i in range(1, n):
		for j in range(i-1, -1, -1):
			if dp[j] and j + nums[j] >= i:
				print(dp[j], f"{j} + {nums[j]} = {j + nums[j]}", i)
				dp[i] = True
				break


	return dp[n - 1]

print(canJump([2, 3, 1, 1, 4]))  # Output: True
print(canJump([3, 2, 1, 0, 4]))  # Output: False