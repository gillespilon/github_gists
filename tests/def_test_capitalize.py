#! /usr/bin/env python3
"""
Test for def capitalize()
"""

import capitalize_string as cs


def test_capital_case():
    '''
    The capitalize() method converts the first character of the string to
    uppercase while making all other characters lowercase.
    '''
    assert cs.capital_case('gilles') == 'Gilles'
    assert cs.capital_case('GILLES') == 'Gilles'
    assert cs.capital_case('gIlLeS') == 'Gilles'
    assert cs.capital_case('Gilles') == 'Gilles'
    assert cs.capital_case('good morning') == 'Good morning'
    assert cs.capital_case('good Morning') == 'Good morning'
    assert cs.capital_case('Good Morning') == 'Good morning'
    assert cs.capital_case('Good morning') == 'Good morning'
