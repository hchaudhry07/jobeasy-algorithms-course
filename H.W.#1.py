# TODO: Homework: Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where User enter n manually. n > 0
# Part 1
from random import randint
from string import digits
n = (input('Input a number of digits'))

y = len(n)
print(y)


def end(y):
    lower_end = 0
    upper_end = 0
    if y >= 0:
        lower_end = 10 ** (y - 1)
        upper_end = ((10 ** (y - 1)) * 10) - 1

    return lower_end, upper_end


num_digit = end(y)
print(num_digit[0])
print(num_digit[1])

add_it_up = randint(num_digit[0], num_digit[1])

n_result = str(add_it_up)
print(n_result)


def digit_count(str1):
    sum_of_digit = 0
    for int_1 in str1:
        if int_1.isdigit():
            x = int(int_1)
            sum_of_digit = sum_of_digit + x

    return sum_of_digit

print(digit_count(n_result))

# Part 2

num_1 = int(input("Please Enter the 1st number here: "))
num_2 = int(input("Please Enter the 2nd number here: "))
num_3 = int(input("Please Enter the 3rd number here: "))

three_values = [num_1, num_2, num_3]

print(max(three_values))

# Part 3

number = "330430903484"


def odd_even(number):
    odd_number = 0
    even_number = 0
    for odd in number:
        if odd.isdigit():
            x = int(odd)
            if (x % 2) == 0:
                even_number = even_number + 1

            else:
                odd_number = odd_number + 1

    return odd_number, even_number


even_odd_list = odd_even(number)
print("Number of Odd are",even_odd_list[0])
print("Number of Even are",even_odd_list[1])

