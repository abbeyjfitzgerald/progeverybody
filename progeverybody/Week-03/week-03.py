# start pay calendar

inp = raw_input("Enter Hours: ")
hours = float(inp)
inp = raw_input("Enter Rate :")
rate = float(inp)
if hours <= 40 :
    pay = rate * hours
else :
    pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
print pay