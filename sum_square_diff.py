# You can edit this code and run it right here in the browser!
def sum(an):
	# divides an i.e input by 2 ad checks if it is even or add 
    n = int(an / 2) 
    if an % 2 == 0: 
    	return n * (1 + an)
    else:
		res = n+1
		return  (n * (1+an)) + res

def sum_square(an):
    sum = 0
    for i in range(1, an + 1):
        sum += i ** 2
    return sum

def problem6(an):
    return sum(an) ** 2 - sum_square(an) 

def inp():
	list1= [] 
	test_case_num = input()
	for i in range(test_case_num):
		test_case = input()
		list1.append(test_case)
	for j in list1:
		print problem6(j)

inp()
