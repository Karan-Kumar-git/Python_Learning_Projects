import random
import string

s = input("Enter a string: ")
words = s.split()
coded_words = []
decoded_words =[]
for word in words:
    if len(word)>= 3:
        first_char = word[0]
        core = word[1:] + first_char
        rand_prefix = "".join(random.choices(string.ascii_lowercase, k = 3))
        rand_suffix = "".join(random.choices(string.ascii_lowercase, k = 3))
        new_word = rand_prefix + core + rand_suffix
    elif len(word) == 2:
        new_word = word[1] + word[0]
    else:
        new_word = word
    coded_words.append(new_word)
    
print(" ".join(coded_words))

word = s.strip()
for word in coded_words:
    if len(word) >=3:
        core = word[3:-3] 
        last_char = core[-1]
        new_word = last_char + core[0:-1]
    elif len(word) == 2:
        new_word = word[1] + word[0]
    else:
        new_word = word
    decoded_words.append(new_word)

print(" ".join(decoded_words))


