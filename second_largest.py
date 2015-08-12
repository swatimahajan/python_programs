l = []
input("enter length od the list: ")
l = raw_input("enter elements of list(seprated by space): ")
result = l.split()
l = list(map(int,result))
l.sort()
a=l.pop()
#check if there are more elements as that was poped out,as it was the largest element  
if a in l:
    l= list(set(l))
    f = l.index(a)
    length1 = l[f-1]
    print "the second largest element is :",length1
else:
    length=len(l)
    print "the second largest element is :",l[length-1]
