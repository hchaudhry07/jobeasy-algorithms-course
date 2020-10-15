# 1.Fibonacci
# TODO: HW: Rewrite code, which will return only needed element of Fib sequence
n_digits = int(input("What is the number of your choice? "))

n1, n2 = 0, 1
count = 0

if n_digits <= 0:
   print("Please enter a positive integer")
elif n_digits == 1:
   print("Fibonacci sequence upto",n_digits,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n_digits:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

# 2.Zeros not for Heroes
# Numbers ending with zeros are boring. They might be fun in your world, but not here. Get rid of them. Only the ending ones.
random_value = 560987000
string_value = str(random_value)
string_value = string_value.strip("0")
print(string_value)


# 3.Digital root is the recursive sum of all the digits in a number.
y = int(input("Enter the number that you want to find the digital root of? "))
def root_of_it_all(j):
    end_result = 0
    x = str(j)
    for n in x:
        if n.isdigit():
            single_int = int(n)
            end_result = end_result + single_int

    if len(str(end_result)) > 1:
        end_result = root_of_it_all(end_result)

    return (end_result)

print(root_of_it_all(y))


# CodeWars Problems

