print("Welcome to The Sum Number Program")

keep_going = True
total = 0

while keep_going:
    input_string = input("Please enter a number. Enter 0 to stop\n")
    if input_string == "0":
        keep_going = False
    else:
        x = float(input_string)
        total += x
        
print(f"Sum of numbers entered is {total}")