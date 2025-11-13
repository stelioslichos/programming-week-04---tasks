# Do not touch this line
input_list = list(input("Please enter a list of strings separated by a comma.\ne.g. one,two,three,four,five\n\n").split(','))

min_index = 100
max_index = 0
sum = 0

i = 0

while i < len(input_list):
    sum += len(input_list[i])
    if len(input_list[i]) > max_index:
        max_index = len(input_list[i])

    if len(input_list[i]) < min_index:
        min_index = len(input_list[i])
    i += 1

print(f"The minimum length of a string is {min_index}")
print(f"The maximum length of a string is {max_index}")
print(f"The average length of the strings in the list is {round(sum/len(input_list),2)}")