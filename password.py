import random
import string

lowercase = [random.choice(string.ascii_lowercase) for e in range(3)]
lowercase1 = [random.choice(string.ascii_lowercase) for e in range(4)] 
uppercase = [random.choice(string.ascii_uppercase) for i in range(random.randint(2,6))]
digit = [random.choice(string.digits) for e in range(random.randint(4,7))]
symbols = [random.choice(string.punctuation) for y in range(3)]

shuffle1 = lowercase1 + uppercase + digit + symbols
random.shuffle(shuffle1)
shuffle_L_U = lowercase + shuffle1

if len(shuffle_L_U) <26:
    totaal = 26 - len(shuffle_L_U)
    for i in range(totaal):
        shuffle_L_U.append(random.choice(string.ascii_lowercase))

print(''.join(shuffle_L_U))