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

class b_land(unittest.TestCase): # {{{
    
    def test_NoArgs(self):          self.assertEqual(b.b_land(), '0')
    
    def test_AllZeros(self):        self.assertEqual(b.b_land('00000000'), '0')
    def test_AllOnes(self):         self.assertEqual(b.b_land('11111111'), '1')
    def test_Random(self):          self.assertEqual(b.b_land('10101101'), '0')
    
    def test_BadA(self):
        self.assertRaises(AssertionError, b.b_land, A=0)
        self.assertRaises(AssertionError, b.b_land, A='01012000')
# }}} End of b_land

class b_lnand(unittest.TestCase): # {{{
    
    def test_NoArgs(self):          self.assertEqual(b.b_lnand(), '1')
    
    def test_AllZeros(self):        self.assertEqual(b.b_lnand('00000000'), '1')
    def test_AllOnes(self):         self.assertEqual(b.b_lnand('11111111'), '0')
    def test_Random(self):          self.assertEqual(b.b_lnand('10101101'), '1')
    
    def test_BadA(self):
        self.assertRaises(AssertionError, b.b_lnand, A=0)
        self.assertRaises(AssertionError, b.b_lnand, A='01012000')
# }}} End of b_lnand

class b_lor(unittest.TestCase): # {{{
    
    def test_NoArgs(self):          self.assertEqual(b.b_lor(), '0')
    
    def test_AllZeros(self):        self.assertEqual(b.b_lor('00000000'), '0')
    def test_AllOnes(self):         self.assertEqual(b.b_lor('11111111'), '1')
    def test_Random(self):          self.assertEqual(b.b_lor('10101101'), '1')
    
    def test_BadA(self):
        self.assertRaises(AssertionError, b.b_lor, A=0)
        self.assertRaises(AssertionError, b.b_lor, A='01012000')
# }}} End of b_lor

class b_lnor(unittest.TestCase): # {{{
    
    def test_NoArgs(self):          self.assertEqual(b.b_lnor(), '1')
    
    def test_AllZeros(self):        self.assertEqual(b.b_lnor('00000000'), '1')
    def test_AllOnes(self):         self.assertEqual(b.b_lnor('11111111'), '0')
    def test_Random(self):          self.assertEqual(b.b_lnor('10101101'), '0')
    
    def test_BadA(self):
        self.assertRaises(AssertionError, b.b_lnor, A=0)
        self.assertRaises(AssertionError, b.b_lnor, A='01012000')
# }}} End of b_lnor

class b_lxor(unittest.TestCase): # {{{
    
    def test_NoArgs(self):          self.assertEqual(b.b_lxor(), '0')
    
    def test_AllZeros(self):        self.assertEqual(b.b_lxor('00000000'), '0')
    def test_AllOnes(self):         self.assertEqual(b.b_lxor('11111111'), '0')
    def test_OneOne(self):          self.assertEqual(b.b_lxor('00001000'), '1')
    def test_OddOnes(self):         self.assertEqual(b.b_lxor('10101101'), '1')
    def test_EvenOnes(self):        self.assertEqual(b.b_lxor('10101001'), '0')
    
    def test_BadA(self):
        self.assertRaises(AssertionError, b.b_lxor, A=0)
        self.assertRaises(AssertionError, b.b_lxor, A='01012000')
# }}} End of b_lxor

class b_lnxor(unittest.TestCase): # {{{
    
    def test_NoArgs(self):          self.assertEqual(b.b_lnxor(), '1')
    
    def test_AllZeros(self):        self.assertEqual(b.b_lnxor('00000000'), '1')
    def test_AllOnes(self):         self.assertEqual(b.b_lnxor('11111111'), '1')
    def test_OneOne(self):          self.assertEqual(b.b_lnxor('00001000'), '0')
    def test_OddOnes(self):         self.assertEqual(b.b_lnxor('10101101'), '0')
    def test_EvenOnes(self):        self.assertEqual(b.b_lnxor('10101001'), '1')
    
    def test_BadA(self):
        self.assertRaises(AssertionError, b.b_lnxor, A=0)
        self.assertRaises(AssertionError, b.b_lnxor, A='01012000')
# }}} End of b_lnxor

# }}} End of Logial Operations

# Convertions To Binary Strings {{{

class int_to_b(unittest.TestCase): # {{{
    
    def test_NoArgs(self):          self.assertEqual(b.int_to_b(), '00000000')
    def test_OnlyNum(self):         self.assertEqual(b.int_to_b(5), '00000101')
    def test_WidthLarge(self):      self.assertEqual(b.int_to_b(0xF5, width=10), '0011110101')
    def test_WidthSmall(self):      self.assertEqual(b.int_to_b(0xF5, width=2), '01')
    def test_EndianBig(self):       self.assertEqual(b.int_to_b(0xF5, endian='big'), '11110101')
    def test_EndianLittle(self):    self.assertEqual(b.int_to_b(0xF5, endian='little'), '10101111')
    def test_ChopMost(self):        self.assertEqual(b.int_to_b(0xF5, width=7, chop='most'), '1110101')
    def test_ChopLeast(self):       self.assertEqual(b.int_to_b(0xF5, width=7, chop='least'), '1111010')
    
    def test_BadNum(self):
        self.assertRaises(AssertionError, b.int_to_b, num=-5)
        self.assertRaises(AssertionError, b.int_to_b, num='5')
    
    def test_BadWidth(self):
        self.assertRaises(AssertionError, b.int_to_b, num=5, width=-5)
        self.assertRaises(AssertionError, b.int_to_b, num=5, width='5')
    
    def test_BadEndian(self):
        self.assertRaises(AssertionError, b.int_to_b, num=5, endian=5)
        self.assertRaises(AssertionError, b.int_to_b, num=5, endian='other')
    
    def test_BadChop(self):
        self.assertRaises(AssertionError, b.int_to_b, num=5, chop=5)
        self.assertRaises(AssertionError, b.int_to_b, num=5, chop='other')
# }}} End of int_to_b

class frac_to_b(unittest.TestCase): # {{{
    
    def test_NoArgs(self):          self.assertEqual(b.frac_to_b(), '00000000')
    def test_OnlyNum(self):         self.assertEqual(b.frac_to_b(0.5), '10000000')
    def test_Width(self):           self.assertEqual(b.frac_to_b(0.5, width=5), '10000')
    def test_EndianBig(self):       self.assertEqual(b.frac_to_b(0.5, endian='big'), '10000000')
    def test_EndianLittle(self):    self.assertEqual(b.frac_to_b(0.5, endian='little'), '00000001')
    
    def test_Rounding(self):
        self.assertEqual(b.frac_to_b(0.3, width=8), '01001101')
        self.assertEqual(b.frac_to_b(0.3, width=5), '01010')
    
    def test_BadNum(self):
        self.assertRaises(AssertionError, b.frac_to_b, num=5)
        self.assertRaises(AssertionError, b.frac_to_b, num='5')
    
    def test_BadWidth(self):
        self.assertRaises(AssertionError, b.frac_to_b, num=5, width=-5)
        self.assertRaises(AssertionError, b.frac_to_b, num=5, width='5')
    
    def test_BadEndian(self):
        self.assertRaises(AssertionError, b.frac_to_b, num=5, endian=5)
        self.assertRaises(AssertionError, b.frac_to_b, num=5, endian='other')
# }}} End of frac_to_b

class str_to_b(unittest.TestCase): # {{{
    
    def test_NoArgs(self):          self.assertEqual(b.str_to_b(), '')
    def test_HexChar(self):         self.assertEqual(b.str_to_b('\x00'), '00000000')
    def test_AsciiChar(self):       self.assertEqual(b.str_to_b('U'), '01010101')
    def test_CharWidthLarge(self):  self.assertEqual(b.str_to_b('U', char_width=9), '001010101')
    def test_CharWidthSmall(self):  self.assertEqual(b.str_to_b('U', char_width=7), '1010101')
    def test_EndianBig(self):       self.assertEqual(b.str_to_b('U', endian='big'), '01010101')
    def test_EndianLittle(self):    self.assertEqual(b.str_to_b('U', endian='little'), '10101010')
    def test_Prefix(self):          self.assertEqual(b.str_to_b('U', prefix='1111'), '111101010101')
    def test_Suffix(self):          self.assertEqual(b.str_to_b('U', suffix='1111'), '010101011111')
    def test_LittlePrefix(self):    self.assertEqual(b.str_to_b('U', endian='little', prefix='1111'), '111110101010')
    def test_LittleSuffix(self):    self.assertEqual(b.str_to_b('U', endian='little', suffix='1111'), '101010101111')
    def test_ParityN(self):         self.assertEqual(b.str_to_b('U', parity='N'), '01010101')
    def test_ParityPO(self):        self.assertEqual(b.str_to_b('U', parity='pO'), '101010101')
    def test_ParitySO(self):        self.assertEqual(b.str_to_b('U', parity='sO'), '010101011')
    def test_ParityPE(self):        self.assertEqual(b.str_to_b('U', parity='pE'), '001010101')
    def test_ParitySE(self):        self.assertEqual(b.str_to_b('U', parity='sE'), '010101010')
    
    def test_BadInstr(self):
        self.assertRaises(AssertionError, b.str_to_b, instr=5)
    
    def test_BadCharWidth(self):
        self.assertRaises(AssertionError, b.str_to_b, instr='\x55', char_width=-5)
        self.assertRaises(AssertionError, b.str_to_b, instr='\x55', char_width='5')
    
    def test_BadEndian(self):
        self.assertRaises(AssertionError, b.str_to_b, instr='\x55', endian=5)
        self.assertRaises(AssertionError, b.str_to_b, instr='\x55', endian='other')
    
    def test_BadPrefix(self):
        self.assertRaises(AssertionError, b.str_to_b, instr='\x55', prefix=5)
        self.assertRaises(AssertionError, b.str_to_b, instr='\x55', prefix='5')
    
    def test_BadSuffix(self):
        self.assertRaises(AssertionError, b.str_to_b, instr='\x55', suffix=5)
        self.assertRaises(AssertionError, b.str_to_b, instr='\x55', suffix='5')
    
    def test_BadParity(self):
        self.assertRaises(AssertionError, b.str_to_b, instr='\x55', parity=5)
        self.assertRaises(AssertionError, b.str_to_b, instr='\x55', parity='5')
# }}} End of str_to_b

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

