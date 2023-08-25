#! /usr/bin/env python3
"""
Function to capitalize a string.
"""


def capital_case(x: str) -> str:
    return x.capitalize()


def main():
    print(capital_case('gilles'))
    print(capital_case('GILLES'))
    print(capital_case('gIlLeS'))
    print(capital_case('good morning'))
    print(capital_case('good Morning'))
    print(capital_case('Good Morning'))
    print(capital_case('Good morning'))


if __name__ == '__main__':
    main()
