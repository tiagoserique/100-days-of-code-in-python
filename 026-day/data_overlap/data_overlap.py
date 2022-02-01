
with open("file1.txt") as file:
    list_1 = file.readlines()

with open("file2.txt") as file:
    list_2 = file.readlines()

result = [int(n) for n in list_1 if ( n in list_2 )]

# Write your code above 👆

print(result)


