# a = 4521369741
# a_list = sum([int(x) for x in str(a)])
# # if len(str(a_list)) > 1:
# #     print(sum([int(x) for x in int(a_list)]))
# # else:
# b = len(a_list)
# print()


# ?
# a = [7, 12, 4, -3, -12]
# print(list(map))




# def sum_of_diff(arr):
#     if len(фкк) <= 1:
#         return 0
#
#     diff = []
#     arr.sort(reverse = True)
#     for i in range(len(arr)):
#         if i + 1 < len(arr):
#             t = abs(arr[i] - arr[i+1])
#             diff(append(t))
#
#     return  sum(diff)
#
# print(sum_of_diff([2,1,10]))

# def fruts(num):




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

