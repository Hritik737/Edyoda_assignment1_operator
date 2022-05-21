# Write a Python program to get the Fibonacci series between 0 to 50.
series=[0,1]
while (series[-1]+series[-2])<50:
    series.append(series[-1]+series[-2])
print(series[1::])