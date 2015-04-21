# Problem Set 2 
# Name: Natalia Prósińska 
# Collaborators: Małgorzata Metryka
# Time Spent: 4:00 

initBal = float(input("What is your outstanding balance on your credit card: "))
intRate = float(input("What is your annual percentage rate (as a decimal, i.e. 18% is .18): "))


montPayment = 10
montIntRate = interestRate/12
bal = initBal

while bal > 0:

   montPayment += 10
   bal = initBal
   numMonths = 0

   while numMonths < 12 and bal > 0:

       numMonths += 1

       int = montIntRate * bal

       bal -= montPayment

       bal += int

bal = round(bal,2)


print ('RESULT')
print ('Monthly payment to pay off debt in 1 year:', montPayment)
print ('Number of months needed:', numMonths)
print ('Balance:', bal)
