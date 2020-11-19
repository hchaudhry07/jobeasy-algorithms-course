# H.W. #6 - Part 1.) -- Write a recursive function to count all the elements in a list (divide and rule).
from math import floor


def element_counting(arr: list):
    if len(arr) == 1:
        return 1
    else:
        midpoint = floor(len(arr) / 2)
        left_side = element_counting(arr[:midpoint])
        right_side = element_counting(arr[midpoint:])
        return left_side + right_side


print(element_counting([55, 27, 38, 49, 95, 100, 2, 51]))


# H.W. #6 - Part 2.) -- Find the biggest number in the list (divide and rule).


def maximum(arr: list):
    if len(arr) == 1:
        return arr[0]
    else:
        midway = floor(len(arr) / 2)
        first_half = maximum(arr[:midway])
        second_half = maximum(arr[midway:])
        return first_half if first_half > second_half else second_half

print(maximum([675, 239235, 75, 2, 45, 99, 230]))


# H.W. #6. - Part 3.) -- There are two lists that have different length. First has keys and the second has values.
# Create a function, which creates a dictionary of keys and values.
# If the is not enough values to match each key, this key should have value equal to None.
# If the is not enough keys to match each value, this value should be ignored.


from pprint import pprint
actors = ['Tom Holland',
          'Chadwick Boseman',
          'Robert Downey Jr.',
          'Scarlett Johansen',
          'Chris Hemsworth',
          'Chris Evans',
          'Mark Ruffalo']

heroes = ['Spider-Man',
          'Black Panther',
          'Iron Man',
          'The Black Widow',
          'Thor',
          'Captain America']

def build_dictionary(keys, values):
    result = {}
    index = 0
    while index < len(keys):
        if index < len(values):
            result[keys[index]] = values[index]
        else:
            result[keys[index]] = None
        index += 1
    return result


pprint(build_dictionary(actors, heroes))
