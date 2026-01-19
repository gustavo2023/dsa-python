"""
Problem: Contains Duplicate
LeetCode URL: https://leetcode.com/problems/contains-duplicate/

Description:
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1 = [1, 2, 3, 1]
    print(f"Test 1: {sol.containsDuplicate(nums1)} (Expected: True)")

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print(f"Test 2: {sol.containsDuplicate(nums2)} (Expected: False)")
