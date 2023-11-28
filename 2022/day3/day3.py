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
for line in file_contents:
    first_set = set()
    second_set = set()
    first_half = line[: len(line) // 2]
    second_half = line[len(line) // 2 :]
    print(first_half)
    print(second_half)
    for char in first_half:
        first_set.add(char)
    for char in second_half:
        second_set.add(char)
    for char in second_set:
        set_length = len(first_set)
        first_set.add(char)
        if len(first_set) == set_length:
            print(char)
            if char in lowercase_mapping:
                sum += lowercase_mapping[char]
            else:
                sum += uppercase_mapping[char]
            break
print(sum)
