#!/usr/bin/env python
# python 3 script

import re
import sys


def showUsage(cmdName):

    if type(cmdName) is not str:
        return -1

    content = '''Usage:
    %s LEVEL [ALIGN]

Where,
    LEVEL   How many levels of Yang Hui's Triangle would you like to print.
            It should be an int number larger than 0.
    ALIGN   How to align the output. Valid values are: left, center.
            It is left by default.

Example:
    %s 9
    %s 5 left
    %s 10 center
'''

    print(content % (cmdName, cmdName, cmdName, cmdName))
    return -1


def alignCenter(string, length):

    if length < len(string):
        length = len(string)

    leftSpaces = (length - len(string)) // 2
    rightSpaces = length - leftSpaces - len(string)

    return ' ' * leftSpaces + string + ' ' * rightSpaces


if len(sys.argv) != 2 and len(sys.argv) != 3:
    exit(showUsage(sys.argv[0]))

level = sys.argv[1].strip()
if not re.match(r'^\d+$', level) or int(level) < 1:
    print('Error: Level [%s] is not valid!\n' % level)
    exit(showUsage(sys.argv[0]))
else:
    level = int(level)

alignment = 'left'
if len(sys.argv) == 3:
    alignment = sys.argv[2].strip()
    if alignment.lower() not in ['left', 'center']:
        print('Error: Align [%s] is not valid.\n' % alignment)
        exit(showUsage(sys.argv[0]))
    else:
        alignment = alignment.lower()

triangleList = []
numMaxLength = 1
for x in range(0, level):
    if x == 0:
        triangleList.append([1])
    else:
        tmpList = [0]
        tmpList += triangleList[x - 1]
        tmpList.append(0)

        triangleList.append([])
        for y in range(0, len(tmpList) - 1):
            number = tmpList[y] + tmpList[y + 1]
            triangleList[x].append(number)
            if len(str(number)) > numMaxLength:
                numMaxLength = len(str(number))

outList = []
for rowList in triangleList:
    rowString = ''
    for number in rowList:
        rowString += alignCenter(str(number), numMaxLength) + ' '
    outList.append(rowString.strip())

if alignment == 'left':
    print('\n'.join(outList))
else:
    maxLineLength = len(outList[-1])
    outString = ''
    for outRow in outList:
        outString += alignCenter(outRow, maxLineLength) + '\n'
    print(outString)
