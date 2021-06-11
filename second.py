'''
A text file named "hasg_message.txt" contains some text, which needs to be
modified such that every next character is separated by a symbol "#". Write a
function definition for hash_display() in Python that would modify the entire
content of the file hash_message.txt in the desired format and display on the
screen.
'''
# Function Defination

def hash_display():
    with open("hash_message.txt","r+") as file:
        data = file.read()
        file.seek(0)

        for letter in data:

            file.write(letter)

            if letter != " ":
                file.write("#")
                print(letter)
        file.seek(file.tell()-1)

        file.write("")
        file.truncate()


# Calling Function
hash_display()
