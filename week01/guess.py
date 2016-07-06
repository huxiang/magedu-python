#!/usr/bin/env python
# python 3 script

import re
import random

# tunable parameters
maxNumber = 10
maxAttempt = 3

secret = int(maxNumber * random.random())

attempt = 1
while True:
    a = input('Input a number [0-%s]: ' % str(maxNumber))
    a = a.strip()

    if not re.match(r'^\d+$', a):
        print('Error: [%s] is not a number!\n' % a)
        continue

    a = int(a)
    if a < 0 or a > maxNumber:
        print('Error: %s is out of range!\n' % str(a))
        continue

    if attempt == maxAttempt:
        if a == secret:
            print('\n### YOU WIN! ###\n')
        else:
            print('Sorry! You didn\'t get it. The secret number is: %s.\n'
                  % str(secret))
        break
    else:
        if a < secret:
            print('Info: %s is less than the secret number. Try again.'
                  % str(a))
        elif a > secret:
            print('Info: %s is larger than the secret number. Try again.'
                  % str(a))
        else:
            print('\n### YOU WIN! ###\n')
            break

        restChance = maxAttempt - attempt
        if restChance == 1:
            print('Info: You have only the last chance!\n')
        else:
            print('Info: You have %s chances left.\n' % str(restChance))
        attempt += 1
