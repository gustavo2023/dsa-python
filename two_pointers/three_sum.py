"""
Problem: 3Sum
LeetCode URL: https://leetcode.com/problems/3sum/description/

Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return triplets


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = sol.threeSum(nums1)
    print(
        f"Test 1: Input: nums = {nums1}, Output: {result1} (Expected: [[-1, -1, 2], [-1, 0, 1]])"
    )

    # Test Case 2
    nums2 = []
    result2 = sol.threeSum(nums2)
    print(f"Test 2: Input: nums = {nums2}, Output: {result2} (Expected: [])")

    # Test Case 3
    nums3 = [0]
    result3 = sol.threeSum(nums3)
    print(f"Test 3: Input: nums = {nums3}, Output: {result3} (Expected: [])")
