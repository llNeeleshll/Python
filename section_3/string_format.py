for i in range(10):
    print("Number {0:2} squared is {1:2} and cubed is {2:3}".format(i,i**2,i**3))


# {number for format:width of the field}

# Aligning the numerical value to left : "<" Left aligned ">" right aligned and "^" for center aligned
for i in range(10):
    print("Number {0:2} squared is {1:<2} and cubed is {2:^3}".format(i,i**2,i**3))

print()
print("Value of pi is {0}".format(22/7))
print("Value of pi is {0:12f}".format(22/7))
print("Value of pi is {0:12.50f}".format(22/7)) # Here 50 is the precision of the pi
print("Value of pi is {0:89.100f}".format(22/7))
print("Value of pi is {0:.100f}".format(22/7)) # Here 100 is the precision of the pi
