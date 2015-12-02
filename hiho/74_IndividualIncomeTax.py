
tax = input()
income = 0

if (tax <= 45):
    income = 3500 + tax / 0.03
elif (tax <= 345):
    income = 5000 + (tax - 45) / 0.1
elif (tax <= 1245):
    income = 8000 + (tax - 345) / 0.2
elif (tax <= 7745):
    income = 12500 + (tax - 1245) / 0.25
elif (tax <= 13745):
    income = 38500 + (tax - 7745) / 0.3
elif (tax <= 22495):
    income = 58500 + (tax - 13745) / 0.35
else:
    income = 83500 + (tax - 22495) / 0.45

print int(income)
