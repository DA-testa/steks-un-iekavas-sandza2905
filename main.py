from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_char in enumerate(text):

        if next_char in "([{":
            opening_brackets_stack.append(Bracket(next_char, i+1))

        elif next_char in ")]}":
            if not opening_brackets_stack:
                return i+1

            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next_char):
                return i+1

    if opening_brackets_stack:
        return opening_brackets_stack[0].position

    return "Success"

def main():
    text = input()
    if "F" in text:
        filename = input()
        with open(filename, "r") as f:
            for i in f:
                print(find_mismatch(i.strip()) or "Success")
    elif "I" in text:
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)

if __name__ == "__main__":
    main()
