inp = input()

l = len(inp)
if l % 2 == 1:
    l -= 1
l = l//2
if ''.join(reversed(inp[:l])) == inp[-l::]:
    print('Palindrome!')
else:
    print('Nothing special about this string :(')