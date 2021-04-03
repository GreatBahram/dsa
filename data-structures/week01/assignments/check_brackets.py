from typing import NamedTuple, Tuple

PAIR_BRACKETS = ("()", "[]", "{}")


class Bracket(NamedTuple):
    bracket: str
    position: int


def matches(left: Tuple[Bracket, str], right: str) -> bool:
    if isinstance(left, Bracket):
        left = left.bracket
    return f"{left}{right}" in PAIR_BRACKETS


def find_mismatch(text: str) -> Tuple[int, bool]:
    opening_brackets_stack = []

    for idx, char in enumerate(text, start=0):
        if char in "([{":
            opening_brackets_stack.append(Bracket(char, idx))
        elif char in ")]}":
            try:
                open_bracket = opening_brackets_stack.pop()
                is_matched = matches(open_bracket, char)
                if not is_matched:
                    return idx + 1
            except IndexError:
                # When the stack is empty and we're facing with a close bracket
                opening_brackets_stack.append(Bracket(char, idx))
                break
    return (
        True
        if not opening_brackets_stack
        else opening_brackets_stack.pop().position + 1
    )


def main():
    text = input()
    answer = find_mismatch(text)
    if isinstance(answer, bool):
        if answer is True:
            print("Success")
        else:
            print(answer)
    else:
        print(answer)


if __name__ == "__main__":
    main()
