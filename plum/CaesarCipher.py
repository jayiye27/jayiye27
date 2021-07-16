alpha = "abcdefghijklmnopqrstuvwxyz"


def encrypt(cleartext):
    cyphertext = ""
    for char in cleartext:
        if char in alpha:
            newpos = (alpha.find(char) + 13) % 26
            cyphertext += alpha[newpos]

        else:
            cyphertext += char

    return cyphertext


while True:
    print("Caesar Cipher")
    cleartext = input("cleartext: ")
    cleartext = cleartext.lower()
    print("Here you go:", encrypt(cleartext))

