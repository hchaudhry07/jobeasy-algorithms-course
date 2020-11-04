# 1.) Write a Python function, which will count how many times a character (substring) is included in a string. DON’T USE METHOD COUNT

stringA = "eofgregrghiglihrththtjohtjhrogjlgdmfld"
stringB = 't'

def sub_count(str1,str2):
    counter = 0
    for x in str1:
        if x == str2:
            counter += 1
    return f'The amount of times that the character, {str2} shows up is: {counter}.'
print(sub_count(stringA,stringB))

#Find and replace a substring in a string for another substring. User enter from a keyboard a string and both substrings. DON’T USE METHOD REPLACE

string1 = input("Enter a sequence of Characters: ")
string2 = input("Enter the portion you want taken out: ")
string3 = input("Enter some characters that you would like as a replacement: ")

def string_edit(str1,str2,str3):
    temporary = ""
    for i in str1:
        if i or i[range(0,len(str2))] == str2:
            temporary = str1.split(str2)
            final_string = str3.join(temporary)
            return final_string
print(string_edit(string1,string2,string3))

#* TODO: Write a function for decompressing string “a4b3c2d”

stringy = "a4b3c2d"
def decompressed(str1):
    index = -1
    b = ""
    for i in str1:
        index +=1
        if i.isdigit():
            a = int(i)
            string_1 = str1[index-1] * a
            string_2 = b + string_1
            b = string_2
    return string_2 + str1[len(str1)-1]
print(decompressed(stringy))

#Recursion for Fib, factorial, digital root

number = int(input('Enter a number please: '))
def factorial(numerical):
    value = 1
    if numerical < 0:
        print("Error")
    elif numerical == 0:
        return 1
    elif numerical > 0:
        value1 = 0
        value = factorial(numerical-1)*numerical
    return value
print(factorial(number))

def digital_root(x):
    sum_number = 0
    j = str(x)
    for i in j:
        if i.isdigit():
            value = int(i)
            sum_number = sum_number + value
    if len(str(sum_number)) > 1:
        sum_number = digital_root(sum_number)
    return (sum_number)
print(digital_root(7))
