class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # length m in matrix
        for i in range(len(matrix)):
            #searching through each sorted list in matrix
            if target in matrix[i]:
                return True
        #target not found
        return False