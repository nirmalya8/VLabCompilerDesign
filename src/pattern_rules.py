import re
def check_pattern(inp):
    rule1 = "^a*"
    rule2 = "^a*b+"
    # rule3 = "^(abb)*"
    # if re.match(rule3,inp):
        # return f"The string {inp} has been matched under the rule {rule3}"
    if re.match(rule2,inp):
        return f"The string {inp} has been matched under the rule {rule2}"
    elif re.match(rule1,inp):
        return f"The string {inp} has been matched under the rule {rule1}"
    else:
        return f"The string {inp} has not been matched under any rule"

