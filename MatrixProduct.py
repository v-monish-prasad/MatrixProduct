def findMatrixProduct(matrix, noOfRows, scalar):
    noOfColumns = len(matrix[0])

    for i in range(noOfRows):
        for j in range(noOfColumns):
            matrix[i][j] *= scalar

    return matrix


if __name__ == "__main__":
    noOfRows = int(input("Enter the no.of rows : "))

    matrix = []
    for i in range(noOfRows):
        matrix.append(list(map(int, input().strip('[').strip(']').split(','))))

    B = int(input())

    print(findMatrixProduct(matrix, noOfRows, B))
