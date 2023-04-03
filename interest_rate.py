#calculating interest rate

t_total = 5 #total time in years
interest_rate = 0.05 #annual interest rate
funds_t0 = 1500 #total funds at time 0
funds = funds_t0 #set the current funds to funds at time 0

for dt in range(t_total):
    funds = funds_t0*interest_rate
print(funds)