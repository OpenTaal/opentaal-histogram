#!/usr/bin/env python3
'''Test checker cache.'''

from cProfile import run

from opentaal import Checker


def test(filename):
    print(filename)
    progress = 0
    with open(filename) as file:
        for line in file:
            word = line[:-1]
            checker.check(word)
            checker.suggest(word)
            checker.check(word)
            checker.suggest(word)
            progress += 1
            if progress % 500 == 0:
                print(progress)
            if progress == 4000:
                break

def main():
    test('../opentaal-wordlist/elements/flexies-ongekeurd.txt')
    test('../opentaal-wordlist/elements/corrections.tsv')

checker = Checker()
run('main()')
