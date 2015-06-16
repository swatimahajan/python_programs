def my_fun(a,b,c):
	print "A simple function"
	print "a:",a
	print "b:", b
	print "c:" ,c
my_fun(*[1],**{"b":8,"c":5})
