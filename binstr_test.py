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
    def test_MixChars(self):        self.assertEqual(b.str_to_b('\x00abc\x55'), '0000000001100001011000100110001101010101')
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

class bytes_to_b(unittest.TestCase): # {{{
    
    def test_NoArgs(self):          self.assertEqual(b.bytes_to_b(), '')
    def test_HexChar(self):         self.assertEqual(b.bytes_to_b(b'\x00'), '00000000')
    def test_MixChars(self):        self.assertEqual(b.bytes_to_b(b'\x00abc\x55'), '0000000001100001011000100110001101010101')
    def test_AsciiChar(self):       self.assertEqual(b.bytes_to_b(b'U'), '01010101')
    def test_CharWidthLarge(self):  self.assertEqual(b.bytes_to_b(b'U', char_width=9), '001010101')
    def test_CharWidthSmall(self):  self.assertEqual(b.bytes_to_b(b'U', char_width=7), '1010101')
    def test_EndianBig(self):       self.assertEqual(b.bytes_to_b(b'U', endian='big'), '01010101')
    def test_EndianLittle(self):    self.assertEqual(b.bytes_to_b(b'U', endian='little'), '10101010')
    def test_Prefix(self):          self.assertEqual(b.bytes_to_b(b'U', prefix='1111'), '111101010101')
    def test_Suffix(self):          self.assertEqual(b.bytes_to_b(b'U', suffix='1111'), '010101011111')
    def test_LittlePrefix(self):    self.assertEqual(b.bytes_to_b(b'U', endian='little', prefix='1111'), '111110101010')
    def test_LittleSuffix(self):    self.assertEqual(b.bytes_to_b(b'U', endian='little', suffix='1111'), '101010101111')
    def test_ParityN(self):         self.assertEqual(b.bytes_to_b(b'U', parity='N'), '01010101')
    def test_ParityPO(self):        self.assertEqual(b.bytes_to_b(b'U', parity='pO'), '101010101')
    def test_ParitySO(self):        self.assertEqual(b.bytes_to_b(b'U', parity='sO'), '010101011')
    def test_ParityPE(self):        self.assertEqual(b.bytes_to_b('U', parity='pE'), '001010101')
    def test_ParitySE(self):        self.assertEqual(b.bytes_to_b('U', parity='sE'), '010101010')
    
    def test_BadInstr(self):
        self.assertRaises(AssertionError, b.bytes_to_b, inbytes=5)
    
    def test_BadCharWidth(self):
        self.assertRaises(AssertionError, b.bytes_to_b, inbytes=b'\x55', char_width=-5)
        self.assertRaises(AssertionError, b.bytes_to_b, inbytes=b'\x55', char_width='5')
    
    def test_BadEndian(self):
        self.assertRaises(AssertionError, b.bytes_to_b, inbytes=b'\x55', endian=5)
        self.assertRaises(AssertionError, b.bytes_to_b, inbytes=b'\x55', endian='other')
    
    def test_BadPrefix(self):
        self.assertRaises(AssertionError, b.bytes_to_b, inbytes=b'\x55', prefix=5)
        self.assertRaises(AssertionError, b.bytes_to_b, inbytes=b'\x55', prefix='5')
    
    def test_BadSuffix(self):
        self.assertRaises(AssertionError, b.bytes_to_b, inbytes=b'\x55', suffix=5)
        self.assertRaises(AssertionError, b.bytes_to_b, inbytes=b'\x55', suffix='5')
    
    def test_BadParity(self):
        self.assertRaises(AssertionError, b.bytes_to_b, inbytes=b'\x55', parity=5)
        self.assertRaises(AssertionError, b.bytes_to_b, inbytes=b'\x55', parity='5')
# }}} End of bytes_to_b

class baseX_to_b(unittest.TestCase): # {{{
    
    def test_NoArgs(self):          self.assertEqual(b.baseX_to_b(), '000000')
    def test_EmptyInstr(self):      self.assertEqual(b.baseX_to_b(''), 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')
    def test_EmptyInstrBase4(self):     self.assertEqual(b.baseX_to_b('', base=4), '0123')
    def test_EmptyInstrBase8(self):     self.assertEqual(b.baseX_to_b('', base=8), '01234567')
    def test_EmptyInstrBase16(self):    self.assertEqual(b.baseX_to_b('', base=16), '0123456789ABCDEF')
    def test_EmptyInstrBase32(self):    self.assertEqual(b.baseX_to_b('', base=32), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567')
    def test_EmptyInstrBase64(self):    self.assertEqual(b.baseX_to_b('', base=64),
                                          'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')
    
    def test_Base4(self):           self.assertEqual(b.baseX_to_b('0123', base=4),
                                      '00 01 10 11'.replace(' ', ''))
    
    def test_Base8(self):           self.assertEqual(b.baseX_to_b('01234567', base=8),
                                      '000 001 010 011 100 101 110 111'.replace(' ', ''))
    
    def test_Base16(self):          self.assertEqual(b.baseX_to_b('0123456789ABCDEF', base=16),
                                      '0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111'.replace(' ', ''))
    
    def test_Base32(self):          self.assertEqual(b.baseX_to_b('ABCDEFGHIJKLMNOPQRSTUVWXYZ234567', base=32),
                                      '00000 00001 00010 00011 00100 00101 00110 00111'.replace(' ', '') +
                                      '01000 01001 01010 01011 01100 01101 01110 01111'.replace(' ', '') +
                                      '10000 10001 10010 10011 10100 10101 10110 10111'.replace(' ', '') +
                                      '11000 11001 11010 11011 11100 11101 11110 11111'.replace(' ', ''))
    
    def test_Base64(self):          self.assertEqual(b.baseX_to_b('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/', base=64),
                                      '000000 000001 000010 000011 000100 000101 000110 000111'.replace(' ', '') +
                                      '001000 001001 001010 001011 001100 001101 001110 001111'.replace(' ', '') +
                                      '010000 010001 010010 010011 010100 010101 010110 010111'.replace(' ', '') +
                                      '011000 011001 011010 011011 011100 011101 011110 011111'.replace(' ', '') +
                                      '100000 100001 100010 100011 100100 100101 100110 100111'.replace(' ', '') +
                                      '101000 101001 101010 101011 101100 101101 101110 101111'.replace(' ', '') +
                                      '110000 110001 110010 110011 110100 110101 110110 110111'.replace(' ', '') +
                                      '111000 111001 111010 111011 111100 111101 111110 111111'.replace(' ', ''))
    
    def test_AlphabetBase4(self):   self.assertEqual(b.baseX_to_b('abcd', base=4, alphabet='abcd'),
                                        '00 01 10 11'.replace(' ', ''))
    
    def test_AlphabetBase8(self):   self.assertEqual(b.baseX_to_b('abcdefgh', base=8, alphabet='abcdefgh'),
                                        '000 001 010 011 100 101 110 111'.replace(' ', ''))
    
    def test_AlphabetBase16(self):  self.assertEqual(b.baseX_to_b('abcdefghijklmnop', base=16, alphabet='abcdefghijklmnop'),
                                        '0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111'.replace(' ', ''))
    
    def test_AlphabetBase32(self):  self.assertEqual(b.baseX_to_b('abcdefghijklmnopqrstuvwxyz012345', base=32,
                                                                    alphabet='abcdefghijklmnopqrstuvwxyz012345'),
                                        '00000 00001 00010 00011 00100 00101 00110 00111'.replace(' ', '') +
                                        '01000 01001 01010 01011 01100 01101 01110 01111'.replace(' ', '') +
                                        '10000 10001 10010 10011 10100 10101 10110 10111'.replace(' ', '') +
                                        '11000 11001 11010 11011 11100 11101 11110 11111'.replace(' ', ''))
    
    def test_AlphabetBase64(self):  self.assertEqual(b.baseX_to_b('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-', base=64,
                                                                    alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-'),
                                      '000000 000001 000010 000011 000100 000101 000110 000111'.replace(' ', '') +
                                      '001000 001001 001010 001011 001100 001101 001110 001111'.replace(' ', '') +
                                      '010000 010001 010010 010011 010100 010101 010110 010111'.replace(' ', '') +
                                      '011000 011001 011010 011011 011100 011101 011110 011111'.replace(' ', '') +
                                      '100000 100001 100010 100011 100100 100101 100110 100111'.replace(' ', '') +
                                      '101000 101001 101010 101011 101100 101101 101110 101111'.replace(' ', '') +
                                      '110000 110001 110010 110011 110100 110101 110110 110111'.replace(' ', '') +
                                      '111000 111001 111010 111011 111100 111101 111110 111111'.replace(' ', ''))
    
    def test_PadDefault(self):      self.assertEqual(b.baseX_to_b('A=='), '000000')
    def test_PadOther(self):        self.assertEqual(b.baseX_to_b('A##', pad='#'), '000000')
    
    def test_BadInstr(self):
        self.assertRaises(AssertionError, b.baseX_to_b, instr=5)
    
    def test_BadBase(self):
        self.assertRaises(AssertionError, b.baseX_to_b, instr='2', base='4')
        self.assertRaises(AssertionError, b.baseX_to_b, instr='2', base=5)
    
    def test_BadAlphabet(self):
        self.assertRaises(AssertionError, b.baseX_to_b, instr='2', alphabet=5)
        self.assertRaises(AssertionError, b.baseX_to_b, instr='2', alphabet='5')
    
    def test_BadPad(self):
        self.assertRaises(AssertionError, b.baseX_to_b, instr='2', pad=5)
        self.assertRaises(AssertionError, b.baseX_to_b, instr='2', pad='++')
# }}} End of baseX_to_b

# }}} Convertions To Binary Strings

# Convertions From Binary Strings {{{

class b_to_int(unittest.TestCase): # {{{
    
    def test_NoArgs(self):          self.assertEqual(b.b_to_int(), 0)
    def test_A(self):         self.assertEqual(b.b_to_int('0101'), 5)
    def test_EndianBig(self):       self.assertEqual(b.b_to_int('0101', endian='big'), 5)
    def test_EndianLittle(self):    self.assertEqual(b.b_to_int('0101', endian='little'), 10)
    
    def test_BadA(self):
        self.assertRaises(AssertionError, b.b_to_int, A=0)
        self.assertRaises(AssertionError, b.b_to_int, A='01012000')
    
    def test_BadEndian(self):
        self.assertRaises(AssertionError, b.b_to_int, A='0', endian=5)
        self.assertRaises(AssertionError, b.b_to_int, A='0', endian='other')
# }}} End of b_to_int

class b_to_frac(unittest.TestCase): # {{{
    
    def test_NoArgs(self):          self.assertEqual(b.b_to_frac(), 0.0)
    def test_A(self):         self.assertEqual(b.b_to_frac('0101'), 0.3125)
    def test_EndianBig(self):       self.assertEqual(b.b_to_frac('0101', endian='big'), 0.3125)
    def test_EndianLittle(self):    self.assertEqual(b.b_to_frac('0101', endian='little'), 0.625)
    
    def test_BadA(self):
        self.assertRaises(AssertionError, b.b_to_frac, A=0)
        self.assertRaises(AssertionError, b.b_to_frac, A='01012000')
    
    def test_BadEndian(self):
        self.assertRaises(AssertionError, b.b_to_frac, A='0', endian=5)
        self.assertRaises(AssertionError, b.b_to_frac, A='0', endian='other')
# }}} End of b_to_frac

# }}} End of Convertions From Binary Strings

# Gray Conversion {{{
# }}} End of Gray Conversion

# Arithmetic Operations {{{
# }}} End of Arithmetic Operations

# Miscellaneous Functions {{{
# }}} End of Miscellaneous Functions

if __name__ == '__main__':
    unittest.main()

