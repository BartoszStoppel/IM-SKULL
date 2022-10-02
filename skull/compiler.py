from skullpy.vm import OPCODE


class ParseError(Exception):
    def __init__(self, message):
        super().__init__(message)


def compile(code: str):
    """Compiles source code into a list of tokens."""
    lines = code.splitlines()
    tokens = []
    for line_no, line in enumerate(lines, start=1):
        words = line.split()
        # Raise syntax error if any word other than '💀' or whitespace is found
        if word_set := (set(words) - {"💀"}):
            raise ParseError(f"Invalid token(s) on line {line_no}: {' '.join(word_set)}")
            return False

        num_skulls = len(line.split())
        # Any number of skulls > 9 is used as is
        if num_skulls > 9:
            tokens.append(num_skulls)
        else:
            tokens.append(OPCODE(num_skulls))
    return tokens