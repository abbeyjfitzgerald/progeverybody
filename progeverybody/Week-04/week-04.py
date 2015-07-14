# start pay and overtime calendar

def computepay(h,r):
    if h <= 40 :
        p = r * h
    else :
        p = (40 * r) + ((h - 40) * (r * 1.5))
    return p

try:
    inp = raw_input("Enter Hours: ")
    hours = float(inp)
    inp = raw_input("Enter Rate : ")
    rate = float(inp)
except: 
    print "Error, please enter numeric input"
    quit()

pay = computepay(hours, rate)
print pay