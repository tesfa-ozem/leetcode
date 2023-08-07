'''
Given a string s, return the longest
palindromic
substring
in s.
'''

class Solution:
    def longestPalindrome(self, s: str) :
        '''
        How do we test a palindrome
        Loop through each character
        create another loop to append the next character
        reverse the substring and compare
        if its a palindrome save its results to an array
        '''
        if len(s)<=1:
            return s

        max_palindrome = ''
        for i in range(len(s)):
            # Check palindromes of odd length
            j = 0
            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                j += 1
            if j * 2 - 1 > len(max_palindrome):
                max_palindrome = s[i - j + 1:i + j]

            # Check palindromes of even length
            j = 0
            while i - j >= 0 and i + j + 1 < len(s) and s[i - j] == s[i + j + 1]:
                j += 1
            if j * 2 > len(max_palindrome):
                max_palindrome = s[i - j + 1:i + j + 1]
        return max_palindrome

    def longestPalindromeDp(self, s: str) -> str:
        n = len(s)
        # create a 2D table to store results of subproblems
        dp = [[False] * n for _ in range(n)]
        max_len = 1  # length of longest palindrome substring found so far
        start = 0  # start index of longest palindrome substring found so far
        
        # every single character is a palindrome
        for i in range(n):
            dp[i][i] = True
        
        # check for substrings of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                max_len = 2
                start = i
        
        # check for substrings of length 3 and above
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i+k-1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    if k > max_len:
                        max_len = k
                        start = i
        
        return s[start:start+max_len]

s = "babad"

solution = Solution()
print(solution.longestPalindrome(s))


