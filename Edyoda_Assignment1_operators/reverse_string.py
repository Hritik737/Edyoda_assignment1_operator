# Write a Python program that accepts a word from the user and reverse it
word=input("Enter the word: ")
a=""
for i in range(len(word)):
    a = word[i] + a 
print(a)