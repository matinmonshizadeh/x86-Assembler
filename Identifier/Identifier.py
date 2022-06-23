# author: Matin Monshizadeh
# university: Shiraz University
# field: Computer Engineering
# date: 10/7/2021
# version: 1.0.0
# description: specify that our input can be an identifier in assembly or not
##############################################################################


# conditions:
# They may contain between 1 and 247 characters (done)
# They are not case-sensitive (done)
# The first character must be a letter (A..Z, a..z), underscore (_), @ , ?, or $. Subsequent characters may also be digits (done)
# An identifier cannot be the same as an assembler reserved word (done)


# get input (String)
identifier = input()

# this list contains all characters that we can use as a first variable character
listOfFirstCharacter = ['_', '@', '?', '$', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# this list contains all characters that we can use as a other variable characters
listOfOtherCharacters = ['_', '@', '?', '$', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# we change indentifier characters to lower case characters because variable in assembly are not case sensitive
newIdentifier = identifier.lower()


# checking condition for newIdentifier length
def IdentifierLength(newIdentifier):
    maximumCharacters = 247
    minimumCharacters = 1
    if len(newIdentifier) <= maximumCharacters and len(newIdentifier) >= minimumCharacters:
        return True
    else:

        print(identifier, "isn't between 1 and 247 characters!")
        return False


# checking condition for first variable character
def FirstCharacter(newIdentifier):
    if newIdentifier[0] in listOfFirstCharacter:
        return True
    else:
        print(identifier, "first character isn't right!")
        return False


# checking condition that Subsequent characters be in listOfOtherCharacters list
def SubsequentCharacters(newIdentifier):
    for character in newIdentifier:
        if character not in listOfOtherCharacters:
            print(identifier, "Subsequent characters isn't right!")
            return False

    return True


# checking condition that readfile contains newIdentifier or not
def ReservedWord(newIdentifier):
    # opening a Rwords_in_asm text file
    file = open("Rwords_in_asm.txt", "r")

    # read file content
    readfile = file.read()
    if "\n" + newIdentifier + "\n" in readfile:
        # closing a file
        file.close()
        print(identifier, "is in reserved word list!")
        return False
    else:
        # closing a file
        file.close()
        return True


if IdentifierLength(newIdentifier) and FirstCharacter(newIdentifier) and SubsequentCharacters(newIdentifier) and ReservedWord(newIdentifier) == True:
    print(identifier, "can be an identifier!")
