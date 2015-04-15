def computepay(h,r):
    ot = 0
    p = h*r
    if h > 40:
        ot = (.5*r) *(h-40)
    tp = ot+p
    return tp

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)
p = computepay(h,r)
print "Pay",p