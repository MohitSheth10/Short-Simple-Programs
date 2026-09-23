abc="abcdefghijklmnopqrstuvwxyz"
word=input("Enter word u want to encrypt and send:")
key= int(input("Enter value by which u want to encrypt the text. "))  #:)
encrypted_word=""
for letter in (word):
    if letter.lower() in abc:
        i=abc.index(letter.lower())
        newi=(i+key)%26  # wrap around to the start after z
        newletter=abc[newi]
        if letter.isupper():
            newletter=newletter.upper()
        encrypted_word= encrypted_word +newletter
    else:
        encrypted_word= encrypted_word +letter  # keep spaces, numbers and symbols as they are
print(encrypted_word)
