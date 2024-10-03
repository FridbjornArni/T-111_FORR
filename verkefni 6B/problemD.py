# fribbi
# problem d
y= int(input())
z=input().split(' ')
temp=[]
for x in z:
	temp.append(int(x))
print(str(max(temp))+' '+str(min(temp)))
