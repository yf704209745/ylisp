# YLisp Specification:
#
# atom 1
# string "hello"
# list ()
# lambda (lambda (arg1 arg2) body)
import sys


def parse(code):
    code = code.replace(' ','').replace('\t','').strip()
    print code


def main(argv):
    if len(argv) == 0:
        return  # TODO:REPL mode

    if len(argv) >= 2 and isinstance(argv[1], str):
        parse(argv[1])


if __name__ == "__main__":
    main(sys.argv)
