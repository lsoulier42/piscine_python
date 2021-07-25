import string


def text_analyzer(*dest_str):
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
    if len(dest_str) > 1:
        print("ERROR")
        return
    if len(dest_str) == 0:
        print("What is the text to analyse?")
        str1 = input()
    elif len(dest_str) == 1:
        str1 = dest_str[0]

    nb_char = len(str1)
    nb_upper = 0
    nb_lower = 0
    nb_spaces = 0
    nb_punct = 0
    for c in str1:
        if c.isupper():
            nb_upper += 1
        if c.islower():
            nb_lower += 1
        if c.isspace():
            nb_spaces += 1
        if c in string.punctuation:
             nb_punct += 1
    print("The text contains {} characters:\n- {} upper letters\n- {} lower letters\n- {} punctuation marks\n- {} spaces".format(nb_char, nb_upper, nb_lower, nb_punct, nb_spaces))


if __name__ == "__main__":
    text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")
    text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")
    text_analyzer()
    text_analyzer("Python", "2.0")
    print(text_analyzer.__doc__)
