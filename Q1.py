# 1. Python program to check whether the given integer is a multiple of 5 and 7 and 10 ,56.

def multiple(num):
    if num % 5 == 0 and num % 7 == 0 and num % 10 == 0 and num % 56 == 0:
        print(f"{num} is a multiple of 5, 7, and 10 , and 56.")
    else:
        print(f"{num} is not a multiple of 5, 7, and 10 , and 56.")
        
        
num = int(input("Enter an integer: "))
multiple(num)


        


