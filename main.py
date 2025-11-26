def main():
    try:
        keyword = getValidInput("Enter keyword for Encryption: ")
        keyword = keyword.upper()
        
        use_keyed = input("Use keyed alphabet for Vigenere Table? (y/N): ").strip()
        if use_keyed.upper() == 'Y':
            while True:
                vKeyword = getValidInput("Enter keyword for Vigenere Table: ")
                vKeyword = vKeyword.upper().replace(" ", "")
                if not hasDuplicateLetters(vKeyword):
                    break
                print("Keyword cannot contain duplicate letters. Please try again.")
            vTable = createVigenereTable(vKeyword)
        else:
            vTable = createNormalVigenereTable()

    except KeyboardInterrupt:
        print("\nExiting...")
        raise


#  Yeah we should definitely use a keyed alphabet for encrypting the plaintext. Dont wanna make things too easy now do we
def createVigenereTable(keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword = keyword.upper()
    for letter in keyword:
        alphabet = alphabet.replace(letter, "")
    alphabet = keyword + alphabet
    table = []
    for i in range(26):
        table.append(alphabet[i:] + alphabet[:i])
    return table


def createNormalVigenereTable():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = []
    for i in range(26):
        table.append(alphabet[i:] + alphabet[:i])
    return table

if __name__ == "__main__":
    main()
