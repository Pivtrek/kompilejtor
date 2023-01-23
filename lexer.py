from sly import Lexer

class mylexer(Lexer):
    tokens = {PROCEDURE, IS, VAR, BEGIN, PROGRAM, END, IF, THEN,
              ELSE, ENDIF, WHILE, DO, ENDWHILE, REPEAT, UNTIL,
              READ, WRITE,
              EQ, NEQ, GT, LS, GEQ, LEQ,
              NUMBER, IDENTIFIER, ASSIGN}
    literals = {'+','-','*','/','%','(',')',',',';'}
    ignore = ' \t'
    ignore_comment = r'\[([^]]|\n)*\]'

    PROCEDURE = r'PROCEDURE'
    IS = r'IS'
    VAR = r'VAR'
    BEGIN = r'BEGIN'
    PROGRAM = r'PROGRAM'
    END = r'END'
    IF = r'IF'
    THEN= r'THEN'
    ELSE = r'ELSE'
    ENDIF = r'ENDIF'
    WHILE = r'WHILE'
    DO = r'DO'
    ENDWHILE = r'ENDWHILE'
    REPEAT = r'REPEAT'
    UNTIL= r'UNTIL'
    READ = r'READ'
    WRITE = r'WRITE'
    EQ = r'='
    NEQ = r'!='
    GT = r'>'
    LS = r'<'
    GEQ = r'>='
    LEQ= r'<='
    NUMBER = r'\d+'
    IDENTIFIER = r'[_a-z]+'
    ASSIGN = r':='

    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1

    
