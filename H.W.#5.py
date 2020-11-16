# H.W. #5 -- Part#1.) -- Last two problems from slides (Sum of odd numbers and Duplicates)
# Write a Python program to remove duplicates from a list.
import string


def clone_removal(string):
    tray = []
    word_list = string.split(' ')
    for word in word_list:
        if word not in tray:
            tray.append(word)
    return ' '.join(tray)


print(clone_removal('Up Left Left Right Left Down Up Right Right Right Down Down Up Left Up Down Right'))


# Given the triangle of consecutive odd numbers:
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:
#
# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8
# row_sum_odd_numbers(3); # 7 + 9 + 11 = 27
# row_sum_odd_numbers(4); # 13 + 15 + 17 + 19 = 64


def odd_numbers_sum(x):
    return x ** 3


print(odd_numbers_sum(1))
print(odd_numbers_sum(2))
print(odd_numbers_sum(3))
print(odd_numbers_sum(4))
print(odd_numbers_sum(5))


# H.W. #5 -- Part#2.) -- When given a list, the program should return a list of all the elements
# that are below the arithmetical mean of the original list.  The arithmetical
# mean is the sum of all elements divided by the number of elements.


def number_reveal(container):

    result = sum(container) / len(container)
    print(result)
    index = -1
    for i in container:
        index += 1
        if i < result:
            container.pop(index)
            return container

print(number_reveal([103,45,89,35]))

# H.W. #5 -- Part#3.) -- When given a list of elements find the two lowest elements. They can be equal to each other or different.

def low_value_2(potato):
    min = potato[0]
    min_2 = potato[0]

    for i in potato:
        if i < min:
            min = i

    for j in potato:
        if min < j < min_2:
            min_2 = j

    return f'The two lowest numbers in the list are: {min} and {min_2}'

print(low_value_2([8,9,4,7,2,1,35,248,.5]))



