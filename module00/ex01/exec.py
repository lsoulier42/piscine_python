import sys

def_wd = ""
i = 0
for wd in sys.argv:
    if i != 0:
        for c in wd[::-1]:
            new_c = ""
            if c.isupper():
                new_c = c.lower()
            else:
                new_c = c.upper()
            def_wd += new_c
        if i != len(sys.argv) - 1:
            def_wd += " "
    i += 1
print(def_wd)
