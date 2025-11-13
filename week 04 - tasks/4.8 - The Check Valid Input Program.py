input_valid = False

while not input_valid:
    num_string = input("Please enter a number:\n")
    try:
        num = float(num_string)
        input_valid = True
    except:
        print("Input is not a valid number.\n")

print(f"{num} + 5 = {num+5}")