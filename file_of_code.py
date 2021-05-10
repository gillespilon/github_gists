#! /usr/bin/env python3
'''
Example of a script with functions.
'''


def main():
    print(capital_case('gilles'))


def capital_case(x: str) -> str:
    return x.capitalize()


if __name__ == '__main__':
    main()
