#calculating interest rate

'''
1. Partner up with one of your neighbors. You only need to have one person coding, but both of you should be able to see the monitor.
2. Calculate by hand the amount of money you’ll have in your account after five years.
3. Download a piece of code which can be found here: LINK TO CODE. Run the code and compare it to your by-hand results.
4. Debug the provided code.
5. Modify the code so that you keep track of all of the values of funds at the different steps.
'''

t_total = 5 #total time in years
interest_rate = 0.05 #annual interest rate
funds_t0 = 1500 #total funds at time 0
funds = funds_t0 #set the current funds to funds at time 0

for dt in range(t_total):
    funds = funds_t0*interest_rate
print(funds)