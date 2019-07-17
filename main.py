import sys

import Figure
import Grammar
import System

def main(args):
    string = args[1]
    grammar = Grammar.Rules(string).apply()
    system = System.Gram()
    system.evaluate(grammar[string])
    Figure.Draw(system)

if __name__== '__main__':
    main(sys.argv)
