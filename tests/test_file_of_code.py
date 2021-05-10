#! /usr/bin/env python3
'''
Test functions for file_of_code.py
'''

import file_of_code as fc


def test_capital_case():
    '''
    The capitalize() method converts the first character of the string to
    uppercase while making all other characters lowercase.
    '''
    assert fc.capital_case('gilles') == 'Gilles'
    assert fc.capital_case('GILLES') == 'Gilles'
    assert fc.capital_case('gIlLeS') == 'Gilles'
    assert fc.capital_case('Gilles') == 'Gilles'
    assert fc.capital_case('good morning') == 'Good morning'
    assert fc.capital_case('good Morning') == 'Good morning'
    assert fc.capital_case('Good Morning') == 'Good morning'
    assert fc.capital_case('Good morning') == 'Good morning'
