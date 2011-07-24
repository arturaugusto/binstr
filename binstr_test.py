#!/usr/bin/env python

###########################################################################
# Copyright (C) 2011  David McEwan
# 
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with this program. If not, see <http://www.gnu.org/licenses/>.
###########################################################################

# Unit tests for Binstr.

import unittest
import binstr as b

# Bitwise Operations {{{

class b_and(unittest.TestCase): # {{{
    
    def test_EqualLengths(self):    self.assertEqual(b.b_and('0101', '0011'), '0001')
    def test_LongerA(self):         self.assertEqual(b.b_and('01010000', '0011'), '00000000')
    def test_LongerB(self):         self.assertEqual(b.b_and('0011', '01010000'), '00000000')
    
    def test_AlignLeft(self):       self.assertEqual(b.b_and('01010000', '0011', align='left'), '00010000')
    def test_AlignRight(self):      self.assertEqual(b.b_and('01010000', '0011', align='right'), '00000000')
    
    def test_NoArgs(self):          self.assertEqual(b.b_and(), '00000000')
    def test_EmptyA(self):          self.assertEqual(b.b_and(B='0101'), '00000000')
    def test_EmptyB(self):          self.assertEqual(b.b_and(A='0101'), '00000000')
    
    def test_BadA(self):
        self.assertRaises(AssertionError, b.b_and, A=0, B='0011')
        self.assertRaises(AssertionError, b.b_and, A='01012000', B='0011')
    def test_BadB(self):
        self.assertRaises(AssertionError, b.b_and, A='01010000', B=0)
        self.assertRaises(AssertionError, b.b_and, A='01010000', B='0021')
    def test_BadAlign(self):
        self.assertRaises(AssertionError, b.b_and, A='01010000', B='0001', align=2)
        self.assertRaises(AssertionError, b.b_and, A='01010000', B='0001', align='bad')
# }}} End of b_and

class b_nand(unittest.TestCase): # {{{
    
    def test_EqualLengths(self):    self.assertEqual(b.b_nand('0101', '0011'), '1110')
    def test_LongerA(self):         self.assertEqual(b.b_nand('01010000', '0011'), '11111111')
    def test_LongerB(self):         self.assertEqual(b.b_nand('0011', '01010000'), '11111111')
    
    def test_AlignLeft(self):       self.assertEqual(b.b_nand('01010000', '0011', align='left'), '11101111')
    def test_AlignRight(self):      self.assertEqual(b.b_nand('01010000', '0011', align='right'), '11111111')
    
    def test_NoArgs(self):          self.assertEqual(b.b_nand(), '11111111')
    def test_EmptyA(self):          self.assertEqual(b.b_nand(B='0101'), '11111111')
    def test_EmptyB(self):          self.assertEqual(b.b_nand(A='0101'), '11111111')
    
    def test_BadA(self):
        self.assertRaises(AssertionError, b.b_nand, A=0, B='0011')
        self.assertRaises(AssertionError, b.b_nand, A='01012000', B='0011')
    def test_BadB(self):
        self.assertRaises(AssertionError, b.b_nand, A='01010000', B=0)
        self.assertRaises(AssertionError, b.b_nand, A='01010000', B='0021')
    def test_BadAlign(self):
        self.assertRaises(AssertionError, b.b_nand, A='01010000', B='0001', align=2)
        self.assertRaises(AssertionError, b.b_nand, A='01010000', B='0001', align='bad')
# }}} End of b_nand

class b_or(unittest.TestCase): # {{{
    
    def test_EqualLengths(self):    self.assertEqual(b.b_or('0101', '0011'), '0111')
    def test_LongerA(self):         self.assertEqual(b.b_or('01010000', '0011'), '01010011')
    def test_LongerB(self):         self.assertEqual(b.b_or('0011', '01010000'), '01010011')
    
    def test_AlignLeft(self):       self.assertEqual(b.b_or('01010000', '0011', align='left'), '01110000')
    def test_AlignRight(self):      self.assertEqual(b.b_or('01010000', '0011', align='right'), '01010011')
    
    def test_NoArgs(self):          self.assertEqual(b.b_or(), '00000000')
    def test_EmptyA(self):          self.assertEqual(b.b_or(B='0101'), '00000101')
    def test_EmptyB(self):          self.assertEqual(b.b_or(A='0101'), '00000101')
    
    def test_BadA(self):
        self.assertRaises(AssertionError, b.b_or, A=0, B='0011')
        self.assertRaises(AssertionError, b.b_or, A='01012000', B='0011')
    def test_BadB(self):
        self.assertRaises(AssertionError, b.b_or, A='01010000', B=0)
        self.assertRaises(AssertionError, b.b_or, A='01010000', B='0021')
    def test_BadAlign(self):
        self.assertRaises(AssertionError, b.b_or, A='01010000', B='0001', align=2)
        self.assertRaises(AssertionError, b.b_or, A='01010000', B='0001', align='bad')
# }}} End of b_or

class b_nor(unittest.TestCase): # {{{
    
    def test_EqualLengths(self):    self.assertEqual(b.b_nor('0101', '0011'), '1000')
    def test_LongerA(self):         self.assertEqual(b.b_nor('01010000', '0011'), '10101100')
    def test_LongerB(self):         self.assertEqual(b.b_nor('0011', '01010000'), '10101100')
    
    def test_AlignLeft(self):       self.assertEqual(b.b_nor('01010000', '0011', align='left'), '10001111')
    def test_AlignRight(self):      self.assertEqual(b.b_nor('01010000', '0011', align='right'), '10101100')
    
    def test_NoArgs(self):          self.assertEqual(b.b_nor(), '11111111')
    def test_EmptyA(self):          self.assertEqual(b.b_nor(B='0101'), '11111010')
    def test_EmptyB(self):          self.assertEqual(b.b_nor(A='0101'), '11111010')
    
    def test_BadA(self):
        self.assertRaises(AssertionError, b.b_nor, A=0, B='0011')
        self.assertRaises(AssertionError, b.b_nor, A='01012000', B='0011')
    def test_BadB(self):
        self.assertRaises(AssertionError, b.b_nor, A='01010000', B=0)
        self.assertRaises(AssertionError, b.b_nor, A='01010000', B='0021')
    def test_BadAlign(self):
        self.assertRaises(AssertionError, b.b_nor, A='01010000', B='0001', align=2)
        self.assertRaises(AssertionError, b.b_nor, A='01010000', B='0001', align='bad')
# }}} End of b_nor

class b_xor(unittest.TestCase): # {{{
    
    def test_EqualLengths(self):    self.assertEqual(b.b_xor('0101', '0011'), '0110')
    def test_LongerA(self):         self.assertEqual(b.b_xor('01010000', '0011'), '01010011')
    def test_LongerB(self):         self.assertEqual(b.b_xor('0011', '01010000'), '01010011')
    
    def test_AlignLeft(self):       self.assertEqual(b.b_xor('01010000', '0011', align='left'), '01100000')
    def test_AlignRight(self):      self.assertEqual(b.b_xor('01010000', '0011', align='right'), '01010011')
    
    def test_NoArgs(self):          self.assertEqual(b.b_xor(), '00000000')
    def test_EmptyA(self):          self.assertEqual(b.b_xor(B='0101'), '00000101')
    def test_EmptyB(self):          self.assertEqual(b.b_xor(A='0101'), '00000101')
    
    def test_BadA(self):
        self.assertRaises(AssertionError, b.b_xor, A=0, B='0011')
        self.assertRaises(AssertionError, b.b_xor, A='01012000', B='0011')
    def test_BadB(self):
        self.assertRaises(AssertionError, b.b_xor, A='01010000', B=0)
        self.assertRaises(AssertionError, b.b_xor, A='01010000', B='0021')
    def test_BadAlign(self):
        self.assertRaises(AssertionError, b.b_xor, A='01010000', B='0001', align=2)
        self.assertRaises(AssertionError, b.b_xor, A='01010000', B='0001', align='bad')
# }}} End of b_xor

class b_nxor(unittest.TestCase): # {{{
    
    def test_EqualLengths(self):    self.assertEqual(b.b_nxor('0101', '0011'), '1001')
    def test_LongerA(self):         self.assertEqual(b.b_nxor('01010000', '0011'), '10101100')
    def test_LongerB(self):         self.assertEqual(b.b_nxor('0011', '01010000'), '10101100')
    
    def test_AlignLeft(self):       self.assertEqual(b.b_nxor('01010000', '0011', align='left'), '10011111')
    def test_AlignRight(self):      self.assertEqual(b.b_nxor('01010000', '0011', align='right'), '10101100')
    
    def test_NoArgs(self):          self.assertEqual(b.b_nxor(), '11111111')
    def test_EmptyA(self):          self.assertEqual(b.b_nxor(B='0101'), '11111010')
    def test_EmptyB(self):          self.assertEqual(b.b_nxor(A='0101'), '11111010')
    
    def test_BadA(self):
        self.assertRaises(AssertionError, b.b_nxor, A=0, B='0011')
        self.assertRaises(AssertionError, b.b_nxor, A='01012000', B='0011')
    def test_BadB(self):
        self.assertRaises(AssertionError, b.b_nxor, A='01010000', B=0)
        self.assertRaises(AssertionError, b.b_nxor, A='01010000', B='0021')
    def test_BadAlign(self):
        self.assertRaises(AssertionError, b.b_nxor, A='01010000', B='0001', align=2)
        self.assertRaises(AssertionError, b.b_nxor, A='01010000', B='0001', align='bad')
# }}} End of b_nxor

class b_not(unittest.TestCase): # {{{
    
    def test_NoArgs(self):          self.assertEqual(b.b_not(), '11111111')
    def test_A(self):               self.assertEqual(b.b_not('0101'), '1010')
    
    def test_BadA(self):
        self.assertRaises(AssertionError, b.b_and, A=0)
        self.assertRaises(AssertionError, b.b_and, A='01012000')
# }}} End of b_not

# }}} End of Bitwise Operations

# Logial Operations {{{
# }}} End of Logial Operations

# Convertions To Binary Strings {{{
# }}} Convertions To Binary Strings

# Convertions From Binary Strings {{{
# }}} End of Convertions From Binary Strings

# Gray Conversion {{{
# }}} End of Gray Conversion

# Arithmetic Operations {{{
# }}} End of Arithmetic Operations

# Miscellaneous Functions {{{
# }}} End of Miscellaneous Functions

if __name__ == '__main__':
    unittest.main()

