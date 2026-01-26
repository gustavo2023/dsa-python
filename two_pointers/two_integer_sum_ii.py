"""
Problem: Two Sum II - Input Array Is Sorted
LeetCode URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Description:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number. Let these two numbers
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer
array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the
same element twice.

Your solution must use only constant extra space.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l + 1, r + 1]


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    result1 = sol.twoSum(numbers1, target1)
    print(
        f"Test 1: Input: numbers = {numbers1}, target = {target1}, Output: {result1} (Expected: [1, 2])"
    )

    # Test Case 2
    numbers2 = [2, 3, 4]
    target2 = 6
    result2 = sol.twoSum(numbers2, target2)
    print(
        f"Test 2: Input: numbers = {numbers2}, target = {target2}, Output: {result2} (Expected: [1, 3])"
    )

    # Test Case 3
    numbers3 = [-1, 0]
    target3 = -1
    result3 = sol.twoSum(numbers3, target3)
    print(
        f"Test 3: Input: numbers = {numbers3}, target = {target3}, Output: {result3} (Expected: [1, 2])"
    )
