word = input('which word would you like to check?')
def palindrome_checker(word):
    length = len(word)
    for i in range (0, (length//2)):
        if word[i] != word[length-i-1]:
            return False
        else:
            return  True
        

if palindrome_checker(word) == True:
    print(word,'is a palindrome')
else:
    print(word,'is not a palindrome')