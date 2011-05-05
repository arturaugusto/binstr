Binstr - A collection of utility functions for creating and operating on
         strings of binary digits. It is compatible with Python versions >2.6
         including 3.x.
         It is useful to use these functions to make small bugs in your code
         easier to find since all inputs are checked thoroughly for errors
         using assertions.

PyPI may not always have the latest version.
The latest version can always be found on the GitHub page (https://github.com/DavidMcEwan/binstr).

Includes:
    int_to_b()      - Convert a positive integer to a sting of binary
                      e.g. int_to_b(5) -> '00000101'
    frac_to_b()     - Convert a positive fraction to a string of binary
                      e.g. frac_to_b(0.5) -> '10000000'
    str_to_b()      - Convert an ASCII string of characters to a string of binary
                      e.g. str_to_b('abc') -> '011000010110001001100011' 
    
    b_land()        - Perform a logical AND
    b_lor()         - Perform a logical OR
    b_lxor()        - Perform a logical XOR
    b_lnand()       - Perform a logical NAND
    b_lnor()        - Perform a logical NOR
    b_lnxor()       - Perform a logical NXOR
    
    b_and()         - Perform a bitwise AND
    b_or()          - Perform a bitwise OR
    b_xor()         - Perform a bitwise XOR
    b_nand()        - Perform a bitwise NAND
    b_nor()         - Perform a bitwise NOR
    b_nxor()        - Perform a bitwise NXOR
    b_not()         - Perform a bitwise NOT (inversion)
    
    b_bin_to_gray() - Convert binary code into gray code
    b_gray_to_bin() - Convert gray code into binary code
    
    b_add()         - Perform an ADD operation
    b_mul()         - Perform a MUL operation (multiply)
    
    b_blockify()    - Separate a string of binary into blocks
    b_validate()    - Validate that a given string contains only 0s and 1s

int_to_b() is a lot more flexible than the built in bin() function although
bin() is used internally. It allows you to force a width, change what bits are
chopped off, change the alignment and change the bit endianness.

The bit endianness is particularly useful for creating binary shuffles.
E.g. For creating the binary shuffle for a 256 sample FFT this can be done in a few lines.

from math import log
length = 256
shuffle = [int( int_to_b(i, width=int(log(length, 2)), endian='little') , 2)
           for i in range(length)]


str_to_b() is also very flexible and can be used to simulate the voltage levels
in serial communication.
E.g. To simulate a standard RS232 port with a "8E1" configuration sending the
data "hello world" this can be done simply.

data = str_to_b('hello_world', endian='little', char_width=8, parity='sE', suffix='1')

Note that data is usually sent out LSB first. The char_width argument is shown
for clarity but is 8 by default. The suffix argument is used to add one stop bit.
-------------------------------------------------------------------------------
Installation
-------------------------------------------------------------------------------
extract the contents of the tarball:
cd to this directory (where README.txt and setup.py are) then run:

python setup.py install

Note: This may need to be run with root (admin) priviliges.
