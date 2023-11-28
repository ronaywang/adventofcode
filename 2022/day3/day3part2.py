# Dictionary mapping lowercase letters to numbers 1-26
lowercase_mapping = {chr(97 + i): i + 1 for i in range(26)}

# Dictionary mapping uppercase letters to numbers 27-52
uppercase_mapping = {chr(65 + i): i + 27 for i in range(26)}

# Open a text file in read mode
file_path = "input.txt"
with open(file_path, "r") as file:
    # Read the contents of the file
    file_contents = file.readlines()
sum = 0
i = 0
while i < len(file_contents):
    first_set = set()
    second_set = set()
    third_set = set()
    first = file_contents[i]
    second = file_contents[i + 1]
    third = file_contents[i + 2]
    overlap_set = set()
    for char in first:
        if char == "\n":
            break
        first_set.add(char)
    for char in second:
        if char == "\n":
            break
        second_set.add(char)
    for char in third:
        if char == "\n":
            break
        third_set.add(char)

    overlap = third_set.intersection(second_set, first_set)
    for char in overlap:
        if char in lowercase_mapping:
            sum += lowercase_mapping[char]
        else:
            sum += uppercase_mapping[char]
    i += 3
print(sum)
