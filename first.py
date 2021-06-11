'''
Jyo has used a text editing software to type some text. After saving the article as
note.txt, she realised that she had wrongly typed alphabet Q in place of alphabet
E everywhere in the article.
Write a function definition for QTOE() in Python that would display the corrected
version of the entire content of the file note.txt with all the alphabets "Q" to be
replaced as an alphabet "E".
'''

# Function definition

def QTOE():
    with open('note.txt', 'r+') as file:
        data = file.read()
        data = data.replace('Q', 'E').replace('q', 'e')
        file.seek(0)
        file.write(data)
        file.truncate()


# calling function
QTOE()
