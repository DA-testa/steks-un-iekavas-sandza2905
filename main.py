# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    mismatches = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))
            

        if next in ")]}":
 if len(opening_brackets_stack) == 0:
                mismatches.append(Bracket(next, i + 1))
            else:
                top = opening_brackets_stack.pop()
                if not are_matching(top.char, next):
                    mismatches.append(Bracket(next, i + 1))
    if len(mismatches) > 0:
        return mismatches[0].position
    elif len(opening_brackets_stack) > 0:
        return opening_brackets_stack[0].position
    else:
        return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == "Success":
        print(mismatch)
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
