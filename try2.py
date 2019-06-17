# erorr with not number value
# print('How many cats do you have?')
# numCats = input()
# if int(numCats) >= 4:
#     print('That is a lot of cats.')
# else:
#     print('That is not that many cats.')

# wrong with negative value
# print('How many cats do you have?')
# numCats = input()
# try:
#     if int(numCats) >= 4:
#         print('That is a lot of cats.')
#     else:
#         print('That is not that many cats.')
# except ValueError:
#     print('You did not enter a number')


print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 0: 
        if int(numCats) >= 4:
            print('That is a lot of cats.')
        else:
            print('That is not that many cats.')
    else:
        print('Negative value is not possible')
except ValueError:
    print('You did not enter a number')