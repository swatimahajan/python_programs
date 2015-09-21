#inp = input()
def power(inp):
	sum_result =0
	for i in range(1,inp+1):
		result = pow(i,i)
		sum_result += result
	a = str(sum_result)
	last_ten_ele = a[-10:]
	if last_ten_ele[0] == '0':
		print last_ten_ele[-9:]
	else:
		print last_ten_ele
inp= input()
power(inp)
