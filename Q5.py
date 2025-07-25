# 5. Write a program.
# For example:
# Input
# [56.2, float('NAN'), 51.7, 55.3, 52.5, float('NAN'), 47.8]
# Output
# [56.2, 51.7, 55.3, 52.5, 47.8]
# Note: No need to input
# -----------------------------------------------------

x = [56.2, float('NAN'), 51.7, 55.3, 52.5, float('NAN'), 47.8]


# example of this :- 
# print(56.20 == 56.20)
# print(float('NAN') == float('NAN'))

for i in x:
    if i == i:  
        print(i)
print() 
