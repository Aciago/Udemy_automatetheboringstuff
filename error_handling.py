"""
def div42by(dividyby):
    return 42 / divideby

print(div42(2))
print(div42(12))
print(div42(0))
print(div42(1))
"""
"""
def div42by(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('Error! You are trying to divide by zero')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
"""

print('How many cats do you have?')
amountCats = input()
try:
    if int(amountCats) >= 4:
        print('Wow, that is a lot of cats!')
    else:
        print('That is not that many cats!')
except ValueError:
    print('You did not enter a number')
