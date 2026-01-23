"""
Problem: Valid Sudoku
LeetCode URL: https://leetcode.com/problems/valid-sudoku/description/

Description:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without
repetition.

Note:

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board)):
                value = board[r][c]

                if value == ".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if value in rows[r] or value in cols[c] or value in boxes[box_index]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                boxes[box_index].add(value)

        return True


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    board1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", "6", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    result1 = sol.isValidSudoku(board1)
    print(f"Test 1: Output: {result1} (Expected: True)")

    # Test Case 2
    board2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", "6", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", "-", "-", "2", "8", "."],
        [".", "-", "-", "4", "1", "9", "-", "-", "5"],
        [".", "-", "-", "-", "8", "-", "-", "7", "9"],
    ]
    result2 = sol.isValidSudoku(board2)
    print(f"Test 2: Output: {result2} (Expected: False)")
