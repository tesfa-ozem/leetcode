def recussion(n:int):
	# print(f'{(n-1)}+{(n-2)}')
	if n<=2:
		return 1
	return recussion(n-1) + recussion(n-2)

nth = recussion(12)

print(nth)