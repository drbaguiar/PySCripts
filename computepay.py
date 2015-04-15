hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)
pay = h* r
if h > 40:
    over_time = float(h - 40)* float(.5 * r)
total_pay = pay + over_time
print total_pay