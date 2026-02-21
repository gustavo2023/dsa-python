"""
Problem: Permutation in String
LeetCode URL: https://leetcode.com/problems/permutation-in-string/description/

Description:
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window, l = len(s1), 0
        count = [0] * 26
        window_count = [0] * 26

        for char in s1:
            count[ord(char) - ord("a")] += 1

        for r in range(len(s2)):
            window_count[ord(s2[r]) - ord("a")] += 1
            window_size = r - l + 1

            if window_size > window:
                index = ord(s2[l]) - ord("a")
                window_count[index] -= 1
                l += 1

            if window_count == count:
                return True

        return False
    

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    s1_1, s2_1 = "ab", "eidbaooo"
    print(sol.checkInclusion(s1_1, s2_1))  # Output: True

    # Test Case 2
    s1_2, s2_2 = "adc", "dcda"
    print(sol.checkInclusion(s1_2, s2_2))  # Output: True

    # Test Case 3
    s1_3, s2_3 = "hello", "oellh"
    print(sol.checkInclusion(s1_3, s2_3))  # Output: True

    # Test Case 4
    s1_4, s2_4 = "abc", "def"
    print(sol.checkInclusion(s1_4, s2_4))  # Output: False
