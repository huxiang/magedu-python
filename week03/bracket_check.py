#!/usr/bin/env python
# python 3 script

bracketMap = {
   '(': ')',
   '[': ']',
   '{': '}',
   '<': '>'
}

inputStr = input('Please input your expression below:\n')

leftBracketList = []
failIndex = None
for idx in range(len(inputStr)):
   if len(leftBracketList) == 0:
      if inputStr[idx] in bracketMap.keys():
         leftBracketList.append(inputStr[idx])
      elif inputStr[idx] in bracketMap.values():
         failIndex = idx
         break

   else:   # leftBracketList is not null
      expRightBracket = bracketMap[leftBracketList[-1]]
      unexpRightBracketList = list(bracketMap.values())
      unexpRightBracketList.remove(expRightBracket)

      if inputStr[idx] in bracketMap.keys():
         leftBracketList.append(inputStr[idx])
      elif inputStr[idx] == expRightBracket:
         leftBracketList.pop()
      elif inputStr[idx] in unexpRightBracketList:
         failIndex = idx
         break
else:
   if len(leftBracketList) != 0:
      failIndex = len(inputStr)

if failIndex is None:
   print('\nNo bracket matching issue found!')
else:
   msg = ' ' * failIndex
   if len(leftBracketList) == 0:
      msg += '^ Left bracket is expected!'
   else:
      msg += '^ "{}" is expected here!'.format(bracketMap[leftBracketList[-1]])
   print(msg)
