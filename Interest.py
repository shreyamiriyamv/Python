principal_amount = float(input("Principal Amount : "))
rate_of_interest = float(input("Rate of Interest : "))
time = float(input("Time (Years) : "))
simple_interest = round(
    ((principal_amount * rate_of_interest * time) / 100), 2)
compound_amount = (principal_amount * (1 + rate_of_interest/100)**time)
compound_interest = round(compound_amount - principal_amount, 2)
print(f"\nSimple Interest : {simple_interest}")
print(f"Compound Interest : {compound_interest}")
