class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #start searching from bottom left of the matrix
        r = len(matrix) - 1 
        c = 0

        while r >= 0 and c < len(matrix[0]):
            if matrix[r][c] == target: #if target found, return True
                return True
            if matrix[r][c] > target: #if target less than current, move upward
                r -= 1
            if matrix[r][c] < target: #if target more than current, move right
                c += 1
        return False
        