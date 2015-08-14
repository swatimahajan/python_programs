ip = raw_input()
s = raw_input()
indx , st = s.split()
string = ip[:int(indx)] + st + ip[int(indx)+1:]
print string
