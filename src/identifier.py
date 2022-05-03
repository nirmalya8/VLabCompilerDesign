import re
RE_Special_Characters = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
RE_Keywords = ["auto","break","case","char","const","continue","default","do","double","else","enum","extern","float","for","goto","if","int","long","register","return","short","signed","sizeof","static","struct","switch","typedef","union","unsigned","void","volatile","while","string","class","struc","include"]
RE_Operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"

def check_identifier(name):
    if name[0].isdigit() or name[0] == '_':
        return f"{name} is an invalid identifier"
    else:
        if re.findall(RE_Operators, name) or re.findall(RE_Special_Characters, name):
            return f"{name} is an invalid identifier"
        elif name in RE_Keywords:
            return f"{name} is an invalid identifier"
        else:
            return f"{name} is an valid identifier"



        