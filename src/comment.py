

def check_comment(line):
    if line[0] == '/':
        if line[1] == '/':
            return f"{line} \nis a single line comment"
        elif line[1] == '*':
            return f"{line} \nis a multi line comment"
        else:
            return f"{line} \nis a string"
    else:
        return f"{line} \nis a string"