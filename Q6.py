# 6. Flatten a list using list comprehension and for a loop.
# For example:
# Input:
# [[1,2,3], [4,5,6], [7,8,9]]
# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Note: No need to input.

# Using list comprehension
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

y = [i for j in x for i in j]
print(y) 



# with loops 
z = []
for i in x:
    for j in i:
        z.append(j)
print(z)