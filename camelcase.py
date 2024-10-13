sentence = input('please type sentence:')
words = sentence.split(' ')
new_sentence = ''
for word in words:
    word = word.capitalize()
    new_sentence = new_sentence+word
print(new_sentence)

'''new_sentence = words[].capitalize() + words[1].capitalize()
print(new_sentence)'''



