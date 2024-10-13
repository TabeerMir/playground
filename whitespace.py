sentence = input('please type sentence:')
for letter in sentence:
    if letter == ' ':
        sentence = sentence.replace(' ','')
print(sentence)