import string
import sys

def print_list(phrase, min_len):
    trail = lambda wd: ''.join([c for c in wd if c not in string.punctuation])
    new_list = [trail(wd) for wd in phrase.split() if len(wd) > min_len]
    print(new_list)


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 3:
        print("ERROR")
    else:
        phrase = sys.argv[1]
        try:
            n = int(sys.argv[2])
            if phrase.isdigit():
                print("ERROR")
            else:
                print_list(phrase, n)
        except BaseException:
            print("ERROR")