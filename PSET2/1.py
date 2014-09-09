balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid = 0
monthlyInterestRate = annualInterestRate / 12.0
for month in range(12):
    minimumMonthlyPayment = monthlyPaymentRate * balance  # PRAVILNO!!!
    totalPaid += minimumMonthlyPayment
    balance -= minimumMonthlyPayment
    balance += balance * monthlyInterestRate
    print "Month: " + str(month+1)
    print "Minimum monthly payment: " + str(round(minimumMonthlyPayment, 2))
    print "Remaining balance: " + str(round(balance, 2))
print "Total paid: " + str(round(totalPaid, 2))
print "Remaining balance: " + str(round(balance, 2))
