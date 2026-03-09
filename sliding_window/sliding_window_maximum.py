"""
Problem: Sliding Window Maximum
LeetCode URL: https://leetcode.com/problems/sliding-window-maximum/description/

Description:
You are given an array of integers nums, there is a sliding window of size k
which is moving from the very left of the array to the very right. You can
only see the k numbers in the window. Each time the sliding window moves
right by one position.

Return the max sliding window.

Time Complexity: O(n)
Space Complexity: O(k)
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l, r = 0, 0
        q = collections.deque()

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3
    result1 = sol.maxSlidingWindow(nums1, k1)
    print(
        f"Test 1: Input: nums={nums1}, k={k1}, Output: {result1} (Expected: [3, 3, 5, 5, 6, 7])"
    )

    # Test Case 2
    nums2 = [1]
    k2 = 1
    result2 = sol.maxSlidingWindow(nums2, k2)
    print(f"Test 2: Input: nums={nums2}, k={k2}, Output: {result2} (Expected: [1])")
