"""
Problem: Longest Repeating Character Replacement
LeetCode URL: https://leetcode.com/problems/longest-repeating-character-replacement/description/

Description:
You are given a string s and an integer k. You can choose any character of the
string and change it to any other uppercase English character. You can perform
this operation at most k times.

Return the length of the longest substring containing the same letter you can
get after performing the above operations.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length, l = 0, 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            replacements = (r - l + 1) - max(count.values())

            if replacements > k:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length
    

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    s1, k1 = "ABAB", 2
    print(sol.characterReplacement(s1, k1))  # Output: 4

    # Test Case 2
    s2, k2 = "AABABBA", 1
    print(sol.characterReplacement(s2, k2))  # Output: 4
