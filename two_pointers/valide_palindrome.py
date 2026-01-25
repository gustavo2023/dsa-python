"""
Problem: Valid Palindrome
LeetCode URL: https://leetcode.com/problems/valid-palindrome/

Description:
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while r > l and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
    

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    s1 = "A man, a plan, a canal: Panama"
    result1 = sol.isPalindrome(s1)
    print(f"Test 1: Input: '{s1}', Output: {result1} (Expected: True)")

    # Test Case 2
    s2 = "race a car"
    result2 = sol.isPalindrome(s2)
    print(f"Test 2: Input: '{s2}', Output: {result2} (Expected: False)")
