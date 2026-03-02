"""
Problem: Minimum Window Substring
LeetCode URL: https://leetcode.com/problems/minimum-window-substring/description/

Description:
Given two strings s and t of lengths m and n respectively, return the minimum
window substring of s such that every character in t (including duplicates)
is included in the window. If there is no such substring, return the empty
string "".

The testcases will be generated such that the answer is unique.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_t, window = {}, {}

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        need, have, l = len(count_t), 0, 0
        res, res_len = [-1, -1], float("infinity")

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = [l, r]

                window[s[l]] -= 1

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1

                l += 1

        if res_len == float("infinity"):
            return ""

        return s[res[0] : res[1] + 1]
    

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    s1, t1 = "ADOBECODEBANC", "ABC"
    print(sol.minWindow(s1, t1))  # Output: "BANC"

    # Test Case 2
    s2, t2 = "a", "a"
    print(sol.minWindow(s2, t2))  # Output: "a"

    # Test Case 3
    s3, t3 = "a", "aa"
    print(sol.minWindow(s3, t3))  # Output: ""
