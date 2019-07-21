import sys

import Figure
import Grammar
import System

def parse(values):
    args = {}
    text = values[1]
    try:
        fmt = values[2]
    except KeyError:
        fmt = None
    args = [text,fmt]
    return args

def main(args):
    args = parse(args)
    string = args[0]
    grammar = Grammar.Rules(string).apply()
    system = System.Gram()
    system.evaluate(grammar[string])
    print args
    if args[1] == 'polar':
        Figure.Polars(system)
    else:
        Figure.Trigrams(system)

if __name__== '__main__':
    main(sys.argv)
