#
# Find out how long to pay off the mortgage

principal = 50000
payment = 2684.50
rate = 0.50
total_paid = 0

# Extra payment
extra_payment = 1000
extra_payment_start_month = 1
extra_payment_end_month = 60
month = 0

out = open('schedule.txt', 'w')          # Open a file for writing
print('{:>5s} {:>10s} {:<10s} {:>1s}'.format('Month', 'Interest', 'Principal', 'Remaining'), file=out)
while principal > 0:
    month += 1
    if extra_payment_start_month <= month <= extra_payment_end_month:
        total_payment = extra_payment + payment
    else:
        total_payment = payment
    interest = principal * (rate/12)
    principal = principal + interest - total_payment
    total_paid += total_payment
    print('{:>5d} {:>10.2f} {:>10.2f} {:>10.2f}'.format(month, interest, total_payment - interest, principal), file=out)

out.close()
print('Total paid: ', total_paid)

