x=3

ans=0

inter=x

print 'Still have ', inter, ' turns left'

while (inter !=0):
    ans = x+ ans
    inter = inter -1
    print x, ans
    if inter >0:
        print 'Still have ', inter, ' turns left'

print 'Done!'