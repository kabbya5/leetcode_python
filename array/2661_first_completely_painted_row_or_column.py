def first_completely_painted_row_or_column(arr,mat):
    m,n = len(mat), len(mat[0])

    value_to_postion = {}

arr = [1, 3, 4, 2]
mat = [[1, 4], [2, 3]]

result = first_completely_painted_row_or_column(arr, mat)
print("Index of first completely painted row or column:", result)