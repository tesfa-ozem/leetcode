from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    row, col = len(matrix), len(matrix[0])

    right, left = 0, col - 1
    up, down = 0, row - 1
    spiral_array = []

    while len(spiral_array) < row * col:
        # Going right
        for i in range(right, left + 1):
            spiral_array.append(matrix[up][i])
        up += 1

        # Moving down
        for i in range(up, down + 1):
            spiral_array.append(matrix[i][left])
        left -= 1

        # Moving left
        for i in range(left, right - 1, -1):
            spiral_array.append(matrix[down][i])
        down -= 1

        # Moving up
        for i in range(down, up - 1, -1):
            spiral_array.append(matrix[i][right])
        right += 1

    return spiral_array

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))


            