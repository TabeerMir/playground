sentence = input('please type sentence in camelcase:')
word = ""
print(sentence) 

for character in sentence:
    if character.isupper() == False: #if this is true there is a new word
        word = word+character
    elif character.isupper() == True:
        word = word+' '+character
print (word)

word = word.strip()
words = word.split(' ')
print (words)
