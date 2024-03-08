#input cost of insurance premiums
rider_before_20 = 196
premium_before_20 = 103
medishield_before_20 = 147

#input medisave interest rates
medisave_interest = 1.04

#number of years you wish to pay for your child
years_to_pay = 12

#amount of money you want to add to his/her medisave
money_in_medisave = 2500

n=1

#assume cost of insurance premiums is fixed at rates in line 1
tot_premiums = premium_before_20+medishield_before_20

while n<=years_to_pay:
  year = n
  premiums_to_date = n*tot_premiums
  add_interest_earn = (money_in_medisave-tot_premiums)*medisave_interest
  money_in_medisave = int(add_interest_earn) #new medisave amount after earn interest
  print(f"year:{n},premiums to date:{premiums_to_date}, money left after premium payment and interest earned:{money_in_medisave}")
  n = n+1
