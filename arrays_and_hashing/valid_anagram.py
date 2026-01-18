"""
Problem: Valid Anagram
LeetCode URL: https://leetcode.com/problems/valid-anagram/description/

Description:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}

        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        return s_dict == t_dict


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    s1, t1 = "anagram", "nagaram"
    print(f"Test 1: {sol.isAnagram(s1, t1)} (Expected: True)")

    # Test Case 2
    s2, t2 = "rat", "car"
    print(f"Test 2: {sol.isAnagram(s2, t2)} (Expected: False)")
