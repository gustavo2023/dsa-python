"""
Problem: Longest Substring Without Repeating Characters
LeetCode URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Description:
Given a string s, find the length of the longest substring without duplicate characters.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length, l, char_set = 0, 0, set()

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    s1 = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s1))  # Output: 3

    # Test Case 2
    s2 = "bbbbb"
    print(sol.lengthOfLongestSubstring(s2))  # Output: 1

    # Test Case 3
    s3 = "pwwkew"
    print(sol.lengthOfLongestSubstring(s3))  # Output: 3
