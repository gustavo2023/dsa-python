"""
Problem: Product of Array Except Self
LeetCode URL: https://leetcode.com/problems/product-of-array-except-self/description/

Description:
Given an integer array nums, return an array answer such that answer[i] is equal to
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix, suffix = 1, 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1 = [1, 2, 3, 4]
    result1 = sol.productExceptSelf(nums1)
    print(f"Test 1: Input: {nums1}, Output: {result1} (Expected: [24, 12, 8, 6])")

    # Test Case 2
    nums2 = [-1, 1, 0, -3, 3]
    result2 = sol.productExceptSelf(nums2)
    print(f"Test 2: Input: {nums2}, Output: {result2} (Expected: [0, 0, 9, 0, 0])")
