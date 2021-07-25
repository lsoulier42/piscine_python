import sys


def get_morse_code():
    morse_code = {}
    code = 'j'
    while code:
        code = input()
        if not code:
            break
        input_code = code.split()
        morse_code[input_code[0]] = input_code[1]
    print(morse_code)


if __name__ == "__main__":
    morse_code = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}
    argc = len(sys.argv)
    stop = False
    if argc > 1:
        for wd in sys.argv:
            if wd == sys.argv[0]:
                continue
            splitted_wd = wd.split()
            for c in splitted_wd:
                if not c.isalnum():
                    print("ERROR")
                    stop = True
        if not stop:
            for wd in sys.argv:
                if wd == sys.argv[0]:
                    continue
                for c in wd:
                    if c.isspace():
                        print(' / ', end='')
                    else:
                        lower_c = c.lower()
                        print(morse_code[lower_c], end='')
                        if c != wd[len(wd) - 1]:
                            print(' ', end='')
                if wd != sys.argv[argc - 1]:
                    print(' / ', end='')
                else:
                    print('')