# 3. Consider the following example of a 3x4 matrix implemented as a list of 3
# lists of length.
# For example:
# Input:
# [
# [1, 2, 3, 4],
# [5, 6, 7, 8],
# [9, 10, 11, 12],
# ]
# Output:
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


x = []
for i in range(len(data[0])): # rows
    y = []
    for j in range(len(data) ): # columns 
         y.append(data[j][i])
    x.append(y)   

print(x) 




