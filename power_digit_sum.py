# computes the sum of digits of 2 to the power n ie. 2*2*2*2 = 16,so result should be 1+6 =7
def power(exp):
	result = pow(2,exp)
	result_list = map(int,list(str(result)))
	sum_digit =0
	for i in result_list:
		sum_digit += i
	return sum_digit
	
	


def inp():
	list1= [] 
	test_case_num = input()
	for i in range(test_case_num):
		test_case = input()
		list1.append(test_case)
	for j in list1:
		print power(j)

inp()
