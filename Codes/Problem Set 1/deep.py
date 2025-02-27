# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

def main():
    feed = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if great(feed):
        print("Yes")
    else:
        print("No")

def great(n):
    match n:
        case "42" | "forty-two" | "forty two":
            return True
        case _:
            return False

main()


# Using if and elif

# Get user input
# answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
# # Print Yes if the user inputs 42 or (case-insensitively) forty-two or forty two
# if answer.strip() == "42":
# print("Yes")
# elif answer. lower().strip() == "forty-two":
# print("Yes")
# elif answer. lower().strip() == "forty two":
# print("Yes")
# # Otherwise output No.
# else:
# print("No")
