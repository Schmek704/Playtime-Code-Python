# Ongese Translator
# Defining the Function
def trans(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "bcdfghjklmnpqrstvwxyz":  # Checking for consonants to add "ong" to the end
            translation = translation + letter + "ong"
        else:
            translation = translation + letter + " "  # if not a consonant then letter in the word remains unchanged
    return translation
# Asking the User for Input

# Introducing the user to the newest language in town!
next = ''
while next.lower() != 'n':
	word = input("\n\nPlease enter a word or phrase:  ")
	print("\n\nWelcome to the world of Ongese!!!")
	print("\nThe translation of your phrase in Ongese is:")
	print("\n\n" + trans(word))
	next = input('\n\nWanna play again??  (y/n)  ')
