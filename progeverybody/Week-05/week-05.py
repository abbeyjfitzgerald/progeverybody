# user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. 

largest = None
smallest = None

while True:
    num = raw_input('Enter a number: ')

    if num == 'done':
        print 'Maximum is %s' % largest
        print 'Minimum is %s' % smallest
        break

    try:
        num = int(num)

        if smallest is None or num <= smallest:
            smallest = num

        if largest is None or num >= largest:
            largest = num

    except:
        print 'Invalid input'