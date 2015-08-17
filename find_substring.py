def occurrences(string, substring):
	l = len(string)
	count = start = 0
	for i in range(l):
		start = string.find(substring, start) + 1
		if start > 0:
			count+=1
		else:
			return count
print occurrences(raw_input(),raw_input())

