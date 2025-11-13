# The Less Rubbish Password Program
# This is the stored password for the user
secret_password = "secret"
access = False

print("Welcome to NOSA Inc.")
print("Did you know that the Moon is an average of 238,855 miles away from Earth")
while not access:
    password = input("\nPlease enter your password:\n")
    
    if password == "secret":
        print("\nAccess Granted!")
        access = True
    else:
        print("\nAccess Denied!")
        
input("\n\nPress the enter key to exit.")