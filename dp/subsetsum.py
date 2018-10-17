def isSubsetSum (items, length, summ):
	if summ == 0:
		return True
	if length == 0 and summ != 0:
		return False

	if (items[length - 1] > summ):
		return isSubsetSum(items, length - 1, summ);

	return isSubsetSum(items, length - 1, summ) or isSubsetSum(items, length - 1, summ - items[length - 1])

if __name__ == '__main__':
	data = [1, 3, 5, 9, 12, 6, 2]
	summ = 11
	length = len(data)

	if (isSubsetSum(data, length, summ) == True):
		print('This set has subsetsum')
	else:
		print('No subsetsum')
