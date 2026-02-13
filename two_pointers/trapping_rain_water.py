"""
Problem: Container With Most Water
LeetCode URL: https://leetcode.com/problems/container-with-most-water/description/

Description:
You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        max_water = 0
        l = 0
        r = len(height) - 1
        left_max = height[l]
        right_max = height[r]

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                max_water += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                max_water += right_max - height[r]

        return max_water


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result1 = sol.trap(height1)
    print(f"Test 1: Input: height = {height1}, Output: {result1} (Expected: 6)")

    # Test Case 2
    height2 = [4, 2, 0, 3, 2, 5]
    result2 = sol.trap(height2)
    print(f"Test 2: Input: height = {height2}, Output: {result2} (Expected: 9)")
