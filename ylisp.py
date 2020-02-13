# YLisp Specification:
#
# atom 1
# string "hello"
# list ()
# lambda (lambda (arg1 arg2) body)
import sys
import re

def yeval(token):
    ctx = {"result":0}

    if isinstance(token,str):
        token = [token]

    i =0
    while i<len(token):
        if token[i]=='+':
            ctx["result"] = yeval(token[i+1])["result"] + yeval(token[i+2])["result"]
            i +=3
        elif token[i]=='-':
            ctx["result"] = yeval(token[i+1])["result"] - yeval(token[i+2])["result"]
            i+=3
        elif token[i]=='*':
            ctx["result"] = yeval(token[i+1])["result"] * yeval(token[i+2])["result"]
            i+=3
        elif token[i]=='/':
            ctx["result"] = yeval(token[i+1])["result"] / yeval(token[i+2])["result"]
            i+=3
        else:
            ctx["result"] = int(token[i])
            i+=2
    return ctx

def parse(code):
    code = code.strip()
    print "Source: " + code
    code=re.sub('\s+',',',code)
    code = code.replace('(','[').replace(')',']').replace(',]',']')
    code = re.sub(r'([+\-*/])',r"'\1'",code) # + => "+"
    code = re.sub(r'(["a-zA-Z0-9_]+)',r"'\1'",code) # ident, 89,"str" = >"ident","89",'"str"'
    code = eval(code)
    print "Tokenized:"+ str(code)
    ctx = yeval(code)
    print ctx

def main(argv):
    if len(argv) == 0:
        return  # TODO:REPL mode

    if len(argv) >= 2 and isinstance(argv[1], str):
        parse(argv[1])


if __name__ == "__main__":
    main(sys.argv)
