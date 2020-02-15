from __future__ import print_function
import sys, re

builtin = {'+': lambda a, b: a + b,
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b,
           '/': lambda a, b: a / b,
           'print': print}


def yeval(token):
    if type(token) == list:
        if type(token[0]) == str and token[0] == 'lambda':
            return {"param": token[1], "body": token[2]}
        else:
            func = yeval(token[0])
            print("Stacktrace:", func, token)
            if type(func) == dict:
                body = str(func["body"])
                for i, name in enumerate(func["param"]):
                    body = body.replace(name, str(yeval(token[i + 1])))
                body = eval(body)
                return yeval(body)
            else:
                return func(*[yeval(t) for t in token[1:]])
    elif builtin.has_key(token):
        return builtin[token]
    elif token.isdigit():
        return int(token)
    elif token.isalpha():
        return token


if __name__ == "__main__" and len(sys.argv) >= 2:
    code = re.sub(r'\s+', ',', sys.argv[1].strip()).replace('(', '[').replace(')', ']').replace(',]', ']')  # type: str
    code = re.sub(r'(["a-zA-Z0-9_]+)', r"'\1'", re.sub(r'([+\-*/])', r"'\1'", code))
    code = eval(code)
    print("Tokenized:" + str(code))
    yeval(code)
