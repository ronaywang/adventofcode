letter_to_num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
strings_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
file_path = "input.txt"
with open(file_path, "r") as file:
    # Read the contents of the file
    file_contents = file.readlines()

sum = 0
for line in file_contents:
    first_digit_found = False
    first_digit = 0
    last_digit = 0
    for char in line:
        if char.isdigit():
            if first_digit_found:
                last_digit = char
            else:
                first_digit = char
                last_digit = char
                first_digit_found = True
    sum += int(first_digit + last_digit)
