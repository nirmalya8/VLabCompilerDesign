

def operator_check(op):
    operator = {'+':"Addition", '-':"Subtract", '*':"Multiply", '/':"Divide", '%':"Modulus",">":"GreaterThan",">=":"Greater Than Or Equal",
    "<":"Less Than","<=":"Less Than Or Equal", "==": "Equal to","++":"Increment by 1", "--":"Decrement by 1","=":"Assignment"
    }

    if op in operator.keys():
        return f"{op} is the {operator[op]} operator."
    else:
        return f"{op} is not an operator."