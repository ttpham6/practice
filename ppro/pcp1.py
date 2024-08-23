
"""
    Python Enhancement Proposal
    
    https://peps.python.org/
    PEP 1   PEP Purpose and Guidelines, which provides information about the purpose of PEPs, their types, and introduces general guidelines;
    PEP 8   Style Guide for Python Code, which gives conventions and presents best practices for Python coding;
    PEP 20  The Zen of Python, which presents a list of principles for Python’s design;
    PEP 257 Docstring Conventions, which provides guidelines for conventions and semantics associated with Python docstrings.
    
    Standards
    Information
    Process 
    
    
"""

import unittest

if False: import this

class PepTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    """
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    """
    def testPep20Beauty(self):
        from math import sqrt
        sidea = float(input("The length of the 'a' side:"))
        sideb = float(input("The length of the 'b' side:"))
        sidec = sqrt(sidea**2+sideb**2)
        print("The length of the hypotenuse is", sidec )
    
    def testPep8(self):
        # You can not mix tabs and spaces
        # PEP requires spaces in place of tabs
        # 4 spaces per indentation
        # Tabs are allowed for backwards compatiblity
        with self.assertRaises(TabError):
		    pass
            # Mixes tab and spaces here
    


    
    
if __name__ == "__main__":
    unittest.main()