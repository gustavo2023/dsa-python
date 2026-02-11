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
    def maxArea(self, height: List[int]) -> int:
        max_container = 0
        l = 0
        r = len(height) - 1

        while l != r:
            min_height = min(height[l], height[r])
            curr_container = (r - l) * min_height

            max_container = max(max_container, curr_container)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_container


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result1 = sol.maxArea(height1)
    print(
        f"Test 1: Input: height = {height1}, Output: {result1} (Expected: 49)"
    )

    # Test Case 2
    height2 = [1, 1]
    result2 = sol.maxArea(height2)
    print(
        f"Test 2: Input: height = {height2}, Output: {result2} (Expected: 1)"
    )