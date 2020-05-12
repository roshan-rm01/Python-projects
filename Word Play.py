def vowels():
    arrvowel = ["a", "e", "i", "o", "u"]
    vowel = str(input("Enter vowel\n"))
    vowel.lower()

    while vowel not in arrvowel:
        print("Invalid input")
        vowel = str(input("Enter vowel\n"))
        vowel.lower()

    while len(vowel) != 1:
        print("Incorrect input")
        vowel = str(input("Enter vowel\n"))
        vowel.lower()

    counter = 0

    for p in enter_word:
        if p == vowel:
            counter += 1
    print("Vowel appears", counter, "time(s)")

    if counter == 0:
        vowels()

    menu()


def palindrome():
    print("Test for palindrome")
    beg = []
    for i in range(len(enter_word)):
        beg.append(enter_word[i])

    rev = []
    for j in range(len(enter_word)):
        rev.append(enter_word[-j - 1])

    if beg == rev:
        print("Word is a palindrome\n")
    else:
        print("Word is not a palindrome\n")

    menu()


def anagram():
    print("Test for anagram")
    test = str(input("Enter another word\n"))

    while len(enter_word) != len(test):
        print("Not the same length")
        test = str(input("Enter another word\n"))

    wordarr = []
    for i in enter_word:
        wordarr.append(i)

    count = 0
    for r in range(0, len(enter_word)):
        if wordarr[r] in test:
            count += 1

    if count == len(enter_word):
        print("Word is an anagram")
    elif count != len(enter_word):
        print("Not an anagram")

    menu()


def leave():
    print("Leaving program")
    exit()


def menu():
    global enter_word
    print("1.Enter a word\n2.Find vowel times\n3.Palindrome\n4.Anagram\n5.Quit")
    select = int(input("Enter Option\n"))

    if select == 1:
        enter_word = str(input("Enter a word\n"))
        print(enter_word)
        menu()
    if select == 2:
        vowels()
    if select == 3:
        palindrome()
    if select == 4:
        anagram()
    if select == 5:
        leave()


menu()
