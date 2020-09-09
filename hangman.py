'''So nice you liked the idea to how this game works. See the code below.'''

word = input('Type the secret word: ').lower().strip()
'''
The ".lower()" is a method returns the lowercased string from the given string. It converts all uppercase characters to lowercase.
The ".strip()" is a method removes characters from both left and right based on the argument.
'''

for w in range(100):
    print()

typed = []
rights = []
wrongs = 0


#The block below is responsible for work and processing of the code, where all the calcs are made:
while True:
    password = ""
    for letter in word:
        password += letter if letter in rights else '.'
    print(password)

    if password == word:
        print("Congratulations! You're right.")
        break

    attempt = input('\nType some letter: ').lower().strip()
    if attempt in word:
        print('Have you tried that letter.')

    else:
        typed += attempt
        if attempt in word:
            rights += attempt

        else:
            wrongs += 1
            print('You missed')


#The block below is responsible for generating the character:
    print('X==:\nX  :  ')
    print('X  O ' if wrongs >= 1 else "X")
    row2 = ""
    if wrongs == 2:
        row2 = "  |  "

    elif wrongs == 3:
        row2 = " \|  "

    elif wrongs >= 4:
        row2 = " \|/ "
    print('X%s' % row2)


    row3 = ""
    if wrongs == 5:
        row3 += " /  "

    elif wrongs >= 6:
        row3 += " / \ "
    print('X%s' % row3)
    print('X\n===========')

    if wrongs == 6:
        print("You was hanged...")
        break
