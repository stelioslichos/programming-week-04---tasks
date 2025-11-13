# Receive and Return
# Demonstrates parameters and return values
def display(message):
    print(message)


def give_me_five():
    return 5


def ask_yes_no(question):
    """Ask a yes or no question."""
    print(question)
    print("\nPlease enter 'y' or 'n': ")
    response = None
    while response not in ("y", "n"):
        response = input().lower()
    return response


# main
display("Here's a message for you.\n")
number = give_me_five()
print("Here's what I got from give_me_five():", number)
answer = ask_yes_no("\nDo you like Python? ")
print("\nThanks for entering:", answer)
input("\n\nPress the enter key to exit.")