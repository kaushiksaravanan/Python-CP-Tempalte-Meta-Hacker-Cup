def test(arr,i,j,n,m):
	i_n=i+1
	j_n=j+1
	i_b=i-1
	j_b=j-1
	c=0
	if i_n<n:
		if arr[i_n][j]=='^':
			c+=1
	if j_n<m:
		if arr[i][j_n]=='^':
			c+=1
	if i_b>=0:
		if arr[i_b][j]=='^':
			c+=1
	if j_b>=0:
		if arr[i][j_b]=='^':
			c+=1
	return c


for _ in range(int(input())):
	k=[int(i) for i in input().split()]
	temp=[]
	for row in range(k[0]):
		temp.append(list(input()))
	# print(temp)
	val=[]
	for row in range(k[0]):
		for letter in range(k[1]):
			# print(letter)
			if temp[row][letter]=='^':
				k_t=test(temp,row,letter,k[0],k[1])
				val.append([[row,letter,k_t]])
	print(val)
	if len(val)==0:
		out='Possible'
	else:
		out='Not'
	print('Case #'+str(_+1)+': '+out)
	if len(val)==0:
		for row in temp:
			for l in row:
				print(l,end='')
			print()
