def check_brackets(x):
    stk = []
    for i in x:
        if i in ["[", "{", "("]:
            stk.append(i)
        else:
            if len(stk) == 0:
                return len(x)
            top = stk.pop(-1)
            if (top == "[" and i != "]") or (top == "{" and i != "}") or (top == "(" and i != ")"):
                return len(x)
    if len(stk) == 0:
        return True
    else:
        return len(x)

x = "{[]})"
print(check_brackets(x))