import sys

from lexer import mylexer
from parser import myparser

if __name__ == '__main__':
    lexer = mylexer()
    parser = myparser()

    file1 = open(sys.argv[1]).read()
    result = 0
    open(sys.argv[2], 'w').write(result)
