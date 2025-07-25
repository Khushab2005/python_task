# 7. To read the last element from each row and sum of the all last elements.
# For example:
# Input
# [[8, 14, -6], [12,7,4], [-11,3,21] ,[12,7,4], [-11,3,21],[12,7,4], [-11,3,21],[12,7,4], [-11,3,21]]
# Output
# 94
# Note: Input should be taken from the terminal.



data = eval(input("Enter: "))

x = []

for i in data:
    x.append(i[-1])
    # print(x)

print(sum(x))
