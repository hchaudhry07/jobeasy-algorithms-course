# 1.) Enter a string of words separated by spaces. Find the longest word. (split / join methods)

def word_search(word):
    word_search = ""
    word_size = 0
    word_list = word.split(" ")

    for words in word_list:
        if (len(words) > word_size):
            word_search = words
            word_search = len(words)

    return word_search
print(word_search("Ice Cream or Cake? Which do you prefer?"))

# 2.) Enter an irregular string (that means it may have space at the beginning of a string, at the end of the string,
# and words may be separated by several spaces).
# Make the string regular (delete all spaces at the beginning and end of the string, leave one space separating words).

def word_spacing(str):

    reduce_word_space = str.strip().split()
    string_result = " "
    string_result = string_result.join(reduce_word_space)
    return string_result
print(word_spacing("   I honestly   can't decide . I   pick both  Ice   Cream  and   Cake."))