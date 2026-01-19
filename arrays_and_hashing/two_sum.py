"""
Problem: Two Sum
LeetCode URL: https://leetcode.com/problems/two-sum/description/

Description:
Given an array of integers nums and an integer target, return indices of the two numbers such
that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in nums_map:
                return [nums_map[difference], i]
            nums_map[nums[i]] = i


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1, target1 = [2, 7, 11, 15], 9
    print(f"Test 1: {sol.twoSum(nums1, target1)} (Expected: [0, 1])")

    # Test Case 2
    nums2, target2 = [3, 2, 4], 6
    print(f"Test 2: {sol.twoSum(nums2, target2)} (Expected: [1, 2])")

    # Test Case 3
    nums3, target3 = [3, 3], 6
    print(f"Test 3: {sol.twoSum(nums3, target3)} (Expected: [0, 1])")
