# Complete a function that takes an input number n such that n >= 10 and n < 10000, then:
#
# Add up all the digits of n.
# Subtract the sum from n and that's your new n.
# If the new n is in the list below, return the fruit associated with it, otherwise return to task 1.
# Example
# n=325
# sum = 3+2+5= 10
# n = 325-10= 315 (not listed)
# sum = 3+1+5= 9
# n = 315-9= 306 (not listed)
# sum = 3+0+6= 9
# n = 306-9= 297 (not listed)
# .
# .
# .
# ...until you find the first n in the list below.
#
# There is no preloaded code to help you. It's not about coding skills; think before you code
#
# 1-kiwi
# 2-pear
# ..............
# 100-pineapple




def getSum(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum

def main():
    number = int(input("Pleas, input any number >= 10 and < 10000:"))
    result = getSum(number)
    print(result)

    result_1 = number - result
    print(result_1)

    list_fruts = ['kiwi',
                  'pear',
                  'kiwi',
                  'banana',
                  'melon',
                  'banana',
                  'melon',
                  'pineapple',
                  'apple',
                  'pineapple',
                  'cucumber',
                  'pineapple',
                  'cucumber',
                  'orange',
                  'grape',
                  'orange',
                  'grape',
                  'apple',
                  'grape',
                  'cherry',
                  'pear',
                  'cherry',
                  'pear',
                  'kiwi',
                  'banana',
                  'kiwi',
                  'apple',
                  'melon',
                  'banana',
                  'melon',
                  'pineapple',
                  'melon',
                  'pineapple',
                  'cucumber',
                  'orange',
                  'apple',
                  'orange',
                  'grape',
                  'orange',
                  'grape',
                  'cherry',
                  'pear',
                  'cherry',
                  'pear',
                  'apple',
                  'pear',
                  'kiwi',
                  'banana',
                  'kiwi',
                  'banana',
                  'melon',
                  'pineapple',
                  'melon',
                  'apple',
                  'cucumber',
                  'pineapple',
                  'cucumber',
                  'orange',
                  'cucumber',
                  'orange',
                  'grape',
                  'cherry',
                  'apple',
                  'cherry',
                  'pear',
                  'cherry',
                  'pear',
                  'kiwi',
                  'pear',
                  'kiwi',
                  'banana',
                  'apple',
                  'banana',
                  'melon',
                  'pineapple',
                  'melon',
                  'pineapple',
                  'cucumber',
                  'pineapple',
                  'cucumber',
                  'apple',
                  'grape',
                  'orange',
                  'grape',
                  'cherry',
                  'grape',
                  'cherry',
                  'pear',
                  'cherry',
                  'apple',
                  'kiwi',
                  'banana',
                  'kiwi',
                  'banana',
                  'melon',
                  'banana',
                  'melon',
                  'pineapple',
                  'apple',
                  'pineapple']
    if result_1 <= 100:
        print(list_fruts[result_1-1])
    else:
        while result_1 > 100:
            total = getSum(result_1)
            result_1 -= total
            print(result_1)
        print(list_fruts[result_1-1])
main()