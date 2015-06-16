i = 0
while i!=2:
	print "who are you ?"
	name =raw_input()
	if name != "Joe":
		i=i+1
		print ("Access Denied" , name)
	      	continue
	print ("Hello Joe  What is the password ?")
	password = raw_input()
	if password == "fish":
		break
	else:
		print ("wrong password")
print ("Access granted ")		