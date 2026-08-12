class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        rowtrack = [0 for _ in range(rows)]
        colstrack = [0 for _ in range(cols)]

        # Track rows and columns containing original zero
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowtrack[i] = -1
                    colstrack[j] = -1

        # Set corresponding rows and columns to zero
        for i in range(rows):
            for j in range(cols):
                if rowtrack[i] == -1 or colstrack[j] == -1:
                    matrix[i][j] = 0