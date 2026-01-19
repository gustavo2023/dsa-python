"""
Problem: Group Anagrams
LeetCode URL: https://leetcode.com/problems/group-anagrams/description/

Description:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Time Complexity:
Space Complexity:
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}

        for string in strs:
            char_count = [0] * 26

            for char in string:
                char_count[ord(char) - ord("a")] += 1

            key = tuple(char_count)

            if key in anagrams_map:
                anagrams_map[key].append(string)
            else:
                anagrams_map[key] = [string]

        return list(anagrams_map.values())


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(
        f"Test 1: {sol.groupAnagrams(strs1)} (Expected: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])"
    )

    # Test Case 2
    strs2 = [""]
    print(f"Test 2: {sol.groupAnagrams(strs2)} (Expected: [['']])")

    # Test Case 3
    strs3 = ["a"]
    print(f"Test 3: {sol.groupAnagrams(strs3)} (Expected: [['a']])")
