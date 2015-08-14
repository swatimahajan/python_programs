def occurrences(string, substring):
	count = start = 0
	while True:
		start = string.find(substring, start) + 1
		if start > 0:
			count+=1
		else:
			return count
print occurrences(raw_input().upper(),raw_input().upper())

