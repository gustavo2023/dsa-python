"""
Problem: Top K Frequent Elements
LeetCode URL: https://leetcode.com/problems/top-k-frequent-elements/description/

Description:
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            frequency_map[n] = frequency_map.get(n, 0) + 1

        for key, value in frequency_map.items():
            buckets[value].append(key)

        most_frequent = []

        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                most_frequent.append(n)

                if len(most_frequent) == k:
                    return most_frequent

        return most_frequent
    

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1, k1 = [1, 1, 1, 2, 2, 3], 2
    print(f"Test 1: {sol.topKFrequent(nums1, k1)} (Expected: [1, 2])")

    # Test Case 2
    nums2, k2 = [1], 1
    print(f"Test 2: {sol.topKFrequent(nums2, k2)} (Expected: [1])")
