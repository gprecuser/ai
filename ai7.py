class Solution:
    def solveNQueens(self, A):
        ans = []
        mat = [["."] * A for _ in range(A)]
        c = set()  # Columns
        d1 = set()  # Diagonal (row - col)
        d2 = set()  # Diagonal (row + col)
       
        def backtrack(row):
            if row == A:
                copy = ["".join(r) for r in mat]
                ans.append(copy)
                return
            for col in range(A):
                if col in c or (row - col) in d1 or (row + col) in d2:
                    continue
                c.add(col)
                d1.add(row - col)
                d2.add(row + col)
                mat[row][col] = "Q"
                backtrack(row + 1)
                mat[row][col] = "."
                c.remove(col)
                d1.remove(row - col)
                d2.remove(row + col)
       
        backtrack(0)
        return ans

# Example usage:
solution = Solution()
result = solution.solveNQueens(4)
for board in result:
    for row in board:
        print(row)
    print()