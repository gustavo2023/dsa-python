"""
Problem: Encode and Decode Strings
LeetCode URL: https://leetcode.com/problems/encode-and-decode-strings/description/

Description:
Design an algorithm to encode a list of strings to a string. The encoded
string is then sent over the network and is decoded back to the
original list of strings.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_str = []

        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            decoded_str.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length

        return decoded_str
    

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    strs1 = ["hello", "world"]
    encoded1 = sol.encode(strs1)
    decoded1 = sol.decode(encoded1)
    print(f"Test 1: Encoded: {encoded1}, Decoded: {decoded1} (Expected: {strs1})")

    # Test Case 2
    strs2 = ["", "a", "bc"]
    encoded2 = sol.encode(strs2)
    decoded2 = sol.decode(encoded2)
    print(f"Test 2: Encoded: {encoded2}, Decoded: {decoded2} (Expected: {strs2})")
