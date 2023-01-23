from sly import Parser

from lexer import mylexer


class myparser(Parser):
    tokens = mylexer.tokens

    @_("procedures main")
    def procmain(self, p):
        pass


'''
    @_("procedures PROCEDURE proc_head IS VAR declarations BEGIN commands END")
    def

    @_("procedures PROCEDURE proc_head IS BEGIN commands END")
    def
    '''


@_("PROGRAM IS VAR declarations BEGIN commands END")
def


@_("PROGRAM IS BEGIN commands END")
def


@_("")
def


@_("declarations identifier")
def


@_("identifier")
def


@_("commands command")
def


@_("command")
def


@_("IF condition THEN commands ELSE commands ENDIF")
def


@_("REPEAT commands UNTIL condition semi")
def
