a,b = input().split()
c = a.replace('5','6' )
d = a.replace('6','5' )
e= b.replace('5','6' )
f= b.replace('6','5')
n_min = int(d)+int(f)
n_max = int(c)+int(e)
print(n_min, n_max)