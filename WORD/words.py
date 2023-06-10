from nltk.corpus import words

easy = [word.lower() for word in words.words() if 3 <= len(word) <= 5]
medium = [word.lower() for word in words.words() if 6 <= len(word) <= 7]
hard = [word.lower() for word in words.words() if 8 <= len(word) <= 9]
impossible = [word.lower() for word in words.words() if len(word) > 9]

e = open('easy.txt', 'w')
m = open('medium.txt', 'w')
h = open('hard.txt', 'w')
i = open('impossible.txt', 'w')

for word in easy:
    e.write(word + '\n')
e.close()
for word in medium:
    m.write(word + '\n')
e.close()
for word in hard:
    h.write(word + '\n')
e.close()
for word in impossible:
    i.write(word + '\n')
e.close()