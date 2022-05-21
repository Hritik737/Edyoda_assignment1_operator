# Write a Python program to count the number of even and odd numbers from a series of numbers.
numbers=(input("enter the numbers: "))
even=0
odd=0
for i in range(len(numbers)):
    if int(numbers[i])%2==0:
        even+=1
    else:
        odd+=1
print("Even",even,"Odd",odd)