"""
Name: Patrick Puckhaber
interest.py

Problem: Computes the monthly interest charge on a credit card account

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    # annual interest rate
    int_rate = eval(input("Please enter Annual Interest Rate as a percent (i.e. 15.84% = 15.84): "))
    # number of days in billing cycle
    billing_cycle = eval(input("How many days are in the billing cycle?: "))
    # previous (net) balance
    prev_bal = eval(input("Please enter the previous (net) balance in:"))
    # payment amount
    pay_amt = eval(input("Enter the payment amount: "))
    # day of the billing cycle that payment was made
    pay_day = eval(input("What day of the billing cycle was payment rendered: "))
    # calculation
    avg_daily = ((prev_bal * billing_cycle) - (pay_amt * (billing_cycle - pay_day))) / billing_cycle
    # monthly interest charge
    interest_amt = avg_daily * ((int_rate / 100) / 12)
    print(round(interest_amt, 2))
