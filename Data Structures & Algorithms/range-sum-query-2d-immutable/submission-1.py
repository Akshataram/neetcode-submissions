class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.pref=[[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(len(matrix)):
            prefix=0
            for j in range(len(matrix[0])):
                prefix+=matrix[i][j]
                above=self.pref[i][j+1]
                self.pref[i+1][j+1]=prefix+above
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottom=self.pref[row2+1][col2+1]
        above=self.pref[row1][col2+1]
        below=self.pref[row2+1][col1]
        minus=self.pref[row1][col1]
        return bottom-above-below+minus

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)