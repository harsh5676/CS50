#In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.

# Convert funtion which converts emoticons into emojis and returns all other text unchanged

def convert(sen):

    sen = sen.replace(":)", "🙂")
    sen = sen.replace(":(", "🙁")
    
    return sen


# Defining main function which takes input from the user

def main():

    sentence = input()

    # Function call for convert function to check the user's input & convert emoticons into emojis present.

    convert(sentence)
    print(sentence)

# Calling main function

main()