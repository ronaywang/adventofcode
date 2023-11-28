# Open a text file in read mode
file_path = "input.txt"
with open(file_path, "r") as file:
    # Read the contents of the file
    file_contents = file.readlines()
max_value = 0
second_max_value = 0
third_max_value = 0
curr = 0
# Print or process the contents
for line in file_contents:
    if line[0] == "\n":  # blank line
        if curr < third_max_value:  # less than third
            curr = 0
            continue
        elif curr < second_max_value:
            third_max_value = curr
        elif curr < max_value:
            third_max_value = second_max_value
            second_max_value = curr
        else:
            third_max_value = second_max_value
            second_max_value = max_value
            max_value = curr
        curr = 0
    else:
        curr += int(line)
print(max_value + second_max_value + third_max_value)
