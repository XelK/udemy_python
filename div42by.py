# error when divide by 0
# def div42by(diviedBy):
#     return 42 / diviedBy

# print (div42by(2))
# print (div42by(12))
# print (div42by(0))
# print (div42by(1))


def div42by(diviedBy):
    try:
        return 42 / diviedBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero')

print (div42by(2))
print (div42by(12))
print (div42by(0))
print (div42by(1))
