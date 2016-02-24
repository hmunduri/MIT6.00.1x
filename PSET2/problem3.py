balance = 5000
annualInterestRate = 0.02
monthlyInterestRate = annualInterestRate / 12.0
tmpBalance = balance
lo = balance / 12.0
hi = balance * (1 + monthlyInterestRate) ** 12 / 12.0
monthlyPayment = round((lo + hi) / 2, 2)
while True:
    monthlyPayment = round((lo + hi) / 2, 2)
    tmpBalance = balance
    for month in range(12):
        tmpBalance -= monthlyPayment
        tmpBalance += tmpBalance * monthlyInterestRate
    if abs(tmpBalance - 0.01) < 0.1:
        print "Lowest Payment: " + str(monthlyPayment)
        break
    elif tmpBalance < 0:
        hi = monthlyPayment
        monthlyPayment = round((lo + hi) / 2, 2)
    else:
        lo = monthlyPayment
        monthlyPayment = round((lo + hi) / 2, 2)
