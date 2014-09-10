monthlyInterestRate = annualInterestRate / 12.0
tmpBalance = balance
monthlyPayment = 0
while tmpBalance > 0:
    tmpBalance = balance
    monthlyPayment += 10
    for month in range(12):
        tmpBalance -= monthlyPayment
        tmpBalance += tmpBalance * monthlyInterestRate
print "Lowest Payment: %i" % monthlyPayment
