# Project name:
Python two-pass assembler.

## Project description:

This project "two-pass assembler" is a project where it uses an input assembly code to 
generate machine code by two passes. Python was used in this project.


## Implementation:
The first pass: scans the assembly code to search for labels and give them their corresponding addresses, 
then proceeds to put them both in a "Symbol table".

The second pass: Python once again scans the assembly code but for instructions to process them,
and proceeds to translate each instruction to binary, while also translating their hexadecimal locations
to binary. This was done by using the "bin" built in function in python.

Python was initially given the basic computer's MRI and non-MRI instructions to be able to 
fetch their symbols and addresses in the scans.

the assembly code was treated as an input file outside of python, then python iterated on each line of the code.

Lastly, the output machine code was written to an output text file "Machine_Code.txt".