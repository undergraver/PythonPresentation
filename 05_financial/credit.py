#!/usr/bin/env python

import math

# user input

moneyAmount=326312
monthsOfCredit=60

# credit details offered by bank

interestRate=5.73 # that is in percent
interestRateIncreaseInMonth=1 # that is in percent - because ROBOR/LIBOR/EURIBOR
monthlyAdministrativeInterestRate=0.04 # that is in percent ( 0.04% )

def GetInterestRate(monthNumber):
    increasedInterestRate = interestRate * pow(1.0+interestRateIncreaseInMonth/100.0,monthNumber)
    return increasedInterestRate


############### start of the simulation ###############

monthlyRateWithNoInterest=float(moneyAmount)/float(monthsOfCredit)

remainingAmount=moneyAmount

totalInterestRateMoney = 0
totalAdminstrationMoney = 0

yearlyPay = 0

for monthNumber in range(monthsOfCredit):

    # since the interest rate is anually we divide by 12
    interestRateMoney = float(remainingAmount) * GetInterestRate(monthNumber) / 100.0 / 12.0

    # bank administration...
    monthlyAdministrativeMoney = float(remainingAmount) * float(monthlyAdministrativeInterestRate) / 100.0

    totalInterestRateMoney = totalInterestRateMoney + interestRateMoney
    totalAdminstrationMoney = totalAdminstrationMoney + monthlyAdministrativeMoney

    totalAmountToPayThiMonth = monthlyRateWithNoInterest + interestRateMoney + monthlyAdministrativeMoney

    yearlyPay = yearlyPay + totalAmountToPayThiMonth

    remainingAmount = remainingAmount - monthlyRateWithNoInterest

    print("%d\t%f\t%f\t%f\t%f\t%f\t(%f)" % (monthNumber+1,remainingAmount,monthlyRateWithNoInterest,interestRateMoney,monthlyAdministrativeMoney, totalAmountToPayThiMonth,GetInterestRate(monthNumber)))

    if (monthNumber+1) % 12 == 0:
        # print interest per year
        extraPercent = 100.0 * (yearlyPay-12.0*monthlyRateWithNoInterest) / (12.0*monthlyRateWithNoInterest)
        print ("Interest per year:%f\n" % (extraPercent))
        yearlyPay = 0
    

totalExtra = totalInterestRateMoney+totalAdminstrationMoney

totalExtraInterestRate = 100.0*float(totalExtra)/float(moneyAmount)

print("Total Interest:%f\nTotal administration:%f\nTotal extra:%f\n" % (totalInterestRateMoney,totalAdminstrationMoney,totalExtra))
print("Total interest rate:%f\n" % (totalExtraInterestRate))


