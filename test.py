
# def fuxk(x):
# 	x *= 2
# 	return x

# print(fuxk(4))

# print(2)
# print(int(3.14))



# listia = [1,2,3]
# listib = [4,5,6]
# listia = listia +['kúkalabbi	']
# listia.append(listib)
# print(listia)


# lst = 'kukalabbi
# lst[-2] = 'ö'
# print(lst)


from copy import deepcopy

zero = [[0] * 3] * 2
sorrow = zero[:]
zorro = deepcopy(sorrow)

zero[0][0] = 1
zero[0].pop()
zero[0].pop()

print(f"Original: {zero}")
print(f"Copy: {sorrow}")
print(f"Deepcopy: {zorro}")
