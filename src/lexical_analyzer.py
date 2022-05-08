import re                                 # for performing regex expressions
RE_Headers = "([a-zA-Z]+\.[h])"
RE_Special_Characters = "[\[@&~!#$\^\|{}\]:;<>?,]|\(\)|\(|\)|{}|\[\]|"
RE_Keywords = "auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|string|class|struc|include"
RE_Operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"
RE_Numerals = "^(\d+)$"
RE_Strings = "\".*\""
RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
def tokenize(source_code):
    tokens = []                               # for string tokens
    # source_code = input()#.split() # turning source code into list of words
    code = ""
    l = ['(',')','"','"',';',',','<','>','+','-','*','/','%','=']
    for i in range(len(source_code)-1):
        if source_code[i+1] in l:
            code = code +source_code[i] + " "
            # code = code  + " "
            # source_code[i+1]
        else:
            if source_code[i] in l:
                code = code +source_code[i] +" "
            else:
                code = code + source_code[i] 
    code+=';'
    print(code)

        
    # word = ""
    # for i in source_code:
    #     if not i==' ' and (re.findall(RE_Operators, i) or re.findall(RE_Special_Characters, i)):
    #         if re.findall(RE_Operators, i):
    #             tokens.append(['Operator',i])
    #         elif re.findall(RE_Special_Characters, i):
    #             tokens.append(['Special Character',i])
    #     elif (re.match("[a-z]", i) or re.match("[A-Z]", i))or re.match(".[0-9]", i):
    #         word += i
    #     if i==' ':
    #         if re.findall(RE_Keywords, word): 
    #             tokens.append(['KEYWORD', word])
    #         elif re.match("[a-z]", word) or re.match("[A-Z]", word):
    #             tokens.append(['IDENTIFIER', word])
    #         elif re.match(".[0-9]", word):
    #             tokens.append(['Numeral', word])
    #         word = ""

    if(source_code[0]=='/' and source_code[1]=='/' or source_code[1]=='*'):
        return "It is a comment"

    # Loop through each source code word.
    code = code.split()
    for word in code:
        
        # This will check if a token has datatype decleration
        if re.findall(RE_Keywords, word): 
            tokens.append(['KEYWORD', word])
        
        # This will look for an identifier which would be just a word
        
        elif re.findall(RE_Identifiers, word):
            tokens.append(['IDENTIFIER', word])
        
        # This will look for an operator
        elif re.findall(RE_Operators, word):
            tokens.append(['OPERATOR', word])


        elif re.findall(RE_Special_Characters, word):
            tokens.append(['Special Character',word])
        

        # This will look for integer items and cast them as a number
        elif re.match(".[0-9]", word):
            if word[len(word) - 1] == ';': 
                tokens.append(["INTEGER", word[:-1]])
            else: 
                tokens.append(["INTEGER", word])

    return tokens # Outputs the token array