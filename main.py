import sys

import Grammar
import Trigram

def main(args):
    s = args[1]
    g = Grammar.Rules(args[1]).apply()
    t = Trigram.Gram()
    f = t.evaluate(g[s])
    t.combine(f)
    Trigram.Draw(t.grams)

if __name__== '__main__':
    main(sys.argv)
