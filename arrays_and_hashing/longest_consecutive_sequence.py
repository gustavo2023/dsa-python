"""
Problem: Longest Consecutive Sequence
LeetCode URL: https://leetcode.com/problems/longest-consecutive-sequence/

Description:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            if n - 1 not in nums_set:
                curr_length = 0

                while n + curr_length in nums_set:
                    curr_length += 1

                longest = max(longest, curr_length)

        return longest


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1 = [100, 4, 200, 1, 3, 2]
    result1 = sol.longestConsecutive(nums1)
    print(f"Test 1: Input: {nums1}, Output: {result1} (Expected: 4)")

    # Test Case 2
    nums2 = [0, -1]
    result2 = sol.longestConsecutive(nums2)
    print(f"Test 2: Input: {nums2}, Output: {result2} (Expected: 2)")
