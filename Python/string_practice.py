name='automation'
print(name[0])
print(name[9])
#or
print(name[-1])
print(name[::-1])

sentence = "python is awesome"
print(sentence.upper())
print(sentence.title())
print(sentence.replace('awesome','powerful'))

fruit = "pineapple"
print(fruit.count('n'))
print(fruit.index('a'))

languages = "Python,Java,SQL"
lst=languages.split()
print(type(lst))


words = ["AK", "will", "crack", "SDET"]
print(' '.join(words))