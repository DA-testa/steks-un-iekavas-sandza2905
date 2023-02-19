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
            if len(opening_brackets_stack) == 0:
                return i+1
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next_char):
                return i+1
    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[0].position
    return "Success"

def main():
    user_input = input("Enter the code: ")
    mismatch = find_mismatch(user_input)
    if mismatch == "Success":
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
