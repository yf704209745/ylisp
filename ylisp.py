# YLisp Specification:
#
# atom 1
# string "hello"
# list ()
# lambda (lambda (arg1 arg2) body)
import sys
import re

builtin={
    '+':lambda a,b:a+b,
    '-':lambda a,b:a-b,
    '*':lambda a,b:a*b,
    '/':lambda a,b:a/b,
}



def yeval(token):
    if isinstance(token, list):
        if isinstance(token[0],str) and token[0]=='lambda':
            return {
                "type": "lambda",
                "param": token[1],
                "body": token[2]
            }
        else:
            func = yeval(token[0])
            if isinstance(func,dict) and func["type"]=="lambda":
                code = func["body"]
                for i,name in enumerate(func["param"]):
                    code = [yeval(token[i+1]) if var==name else var for var in code]
                return yeval(code)
            else:
                return func(token[1],token[2])
    elif token == '+' or token == '-' or token == '*' or token == '/':
        return builtin[token]
    else:
        return int(token)

def parse(code):
    code = re.sub('\s+', ',', code.strip())
    code = code.replace('(', '[').replace(')', ']').replace(',]', ']')
    code = re.sub(r'([+\-*/])', r"'\1'", code)  # + => "+"
    code = re.sub(r'(["a-zA-Z0-9_]+)', r"'\1'", code)  # ident, 89,"str" = >"ident","89",'"str"'
    code = eval(code)
    print "Tokenized:" + str(code)
    ctx = yeval(code)
    print ctx


def main(argv):
    if len(argv) == 0:
        return  # TODO:REPL mode

    if len(argv) >= 2 and isinstance(argv[1], str):
        parse(argv[1])


if __name__ == "__main__":
    main(sys.argv)
