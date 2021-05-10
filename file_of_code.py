#! /usr/bin/env python3
'''
Example of a script with functions.
'''


def main():
    print(capital_case('gilles'))
    print(capital_case('GILLES'))
    print(capital_case('gIlLeS'))
    print(capital_case('good morning'))
    print(capital_case('good Morning'))
    print(capital_case('Good Morning'))
    print(capital_case('Good morning'))


def capital_case(x: str) -> str:
    return x.capitalize()


if __name__ == '__main__':
    main()
