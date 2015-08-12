def user_input():
    input()
    l = raw_input()
    result = l.split()
# map converts input string list into int
    r= list(map(int,result))
    return r
M = user_input()
N =user_input()
print M
print N
# to print unique elements between 2 lists M and N
print sorted(list(set(M).difference(N))+ list(set(N).difference(M)))
for i in a:
    print i
