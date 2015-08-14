inp = input()
for i in range(inp):
    n= raw_input()
    l= list(n.split())
    l2 =map(int, l)
    l3= tuple(l2)
    print hash(l3)
