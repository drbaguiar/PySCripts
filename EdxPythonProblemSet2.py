#Payment schedule
balance = 3200
annualInterestRate = 0.18
monthlyPaymentRate = 0.04

# Start here
totalpaid = 0
months = range(1,13)
for month in months:
    print "Month: ", month
    payment = balance * monthlyPaymentRate
    totalpaid += payment
    print "Minimum monthly payment: " , "%0.2f" % (payment,)
    unpaid = balance-payment
    #print "%0.2f" % interest,
    #print "%0.2f" % (unpaid,)
    interest = unpaid * (annualInterestRate/12)
    balance = unpaid + interest
    print "Remaining balance: " , "%0.2f" % (balance,)

print "Total paid: ", "%0.2f" % (totalpaid,)
print "Remaining balance: " , "%0.2f" % (balance,)

##Problem 2
##Start here
payment = 330
runbalance = 0 
months = range(1,13) 
while True:
    runbalance = balance
    for month in months:
        #print "Month: ", month
        #print "Payment: ", payment
        unpaid = runbalance-payment
        #print "Unpaid: ", unpaid
        interest = unpaid * (annualInterestRate/12)
        #print "Interest: ", interest
        runbalance = unpaid + interest
        if runbalance < 0:
            break
    if runbalance > 0:
        payment = payment + 10
    else:
        break
print "Lowest payment: " , payment

##Problem 3

##Start here
epislon = .02
monthlyInterestRate = annualInterestRate/12
payment = balance / 12 # lower bound
paymentupperbound = (balance * (1 +monthlyInterestRate)**12) / 12.0
runbalance = 0 
months = range(1,13) 

while True:
    runbalance = balance
    for month in months:
        unpaid = runbalance-payment
        interest = unpaid * monthlyInterestRate
        runbalance = unpaid + interest
        #print "Month: ", month, "Payment: ", payment, "Unpaid: ", unpaid,  "Interest: ", interest, "Running Balance: ", runbalance, "Diff: ", runbalance - unpaid
        diff = runbalance - unpaid
        if runbalance <= 0:
            #print "yes"
            break
    if runbalance >= 0:
        if diff < epislon:
            break 
        if payment < paymentupperbound:
            payment += diff
        
    else:
        break
print "Lowest payment: " ,  "%0.2f" % (payment,)