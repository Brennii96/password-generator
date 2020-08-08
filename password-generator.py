import string

from random import choice, randint

characters = string.ascii_letters + string.punctuation + string.digits
for x in range(6):
    print("".join(choice(characters) for x in range(randint(16,28))))
