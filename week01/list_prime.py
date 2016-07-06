#!/usr/bin/env python
# python 3 script

import re
import sys


def showUsage(cmdName):

    if type(cmdName) is not str:
        return -1

    content = '''Usage:
    %s NUMBER

Where,
    NUMBER      You'd like to list prime numbers till which number
                It should be an int number larger than 1

Example:
    %s 100
'''

    print(content % (cmdName, cmdName))
    return -1


if len(sys.argv) != 2:
    exit(showUsage(sys.argv[0]))

number = sys.argv[1].strip()
if not re.match(r'^\d+$', number):
    print('Error: [%s] is not an int number!\n' % number)
    exit(1)

number = int(number)
if number <= 1:
    print('Error: the number should be larger than 1!\n')
    exit(2)

for x in range(2, number + 1):
    if x == 2:
        primeList = [2]
    else:
        for y in primeList:
            if x % y == 0:
                break
        else:
            primeList.append(x)

primeListString = ''
for prime in primeList:
    primeListString += str(prime) + ' '

print(primeListString)
