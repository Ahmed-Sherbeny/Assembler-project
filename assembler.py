#Initialize for ORG 0
LC = 0x0000
sym_table = {}

# Basic computer instructions
mri_table = {
    'AND'  : '0000',
    "ADD": "0001",   # Add to accumulator
    "LDA": "0010",   # Load accumulator
    "STA": "0011",   # Store accumulator
    "BUN" : '0100',  # Branch unconditionally
    "BSA" : '0101',  # Brand and save return address
    "ISZ" : '0110',  # Increment and skip if zero
}

non_mri_table = {
    "CLA": "7800",  # Clear AC
    "CLE": "7400",  # Clear E
    "CMA": "7200",  # Complement AC
    "CME": "7100",  # Complement E
    "CIR": "7080",  # Circulate right AC and E
    "CIL": "7040",  # Circulate left AC and E
    "INC": "7020",  # Increment AC
    "SPA": "7010",  # Skip next instruction if AC is positive
    "SNA": "7008",  # Skip next instruction if AC is negative
    "SZA": "7004",  # Skip next instruction if AC is zero
    "SZE": "7002",  # Skip next instruction if E is 0
    "HLT": "7001",  # Halt computer
    "INP": "F800",  # Input character to AC
    "OUT": "F400",  # Output character from AC
    "SKI": "F200",  # Skip on input flag
    "SKO": "F100",  # Skip on output flag
    "ION": "F080",  # Interrupt on
    "IOF": "F040",  # Interrupt off
}




filename = "assembly.txt"

# First pass
with open(filename) as assembly_file:
    for line in assembly_file:
        token = line.split()
        if line.startswith('ORG'):
            LC = int(token[1], 16) 
            continue

        elif token[0].endswith(','):
            sym_table[token[0].rstrip(',')] = f"0x{hex(LC)[2:]:>04}"

        elif line.startswith('END'):
            break

        LC += 1



print('Symbol table:')
for label, address in sym_table.items():
    print(f"{label}: {address}")

# Second pass
LC = 0
machine_code = {}
with open(filename) as assembly_file:
    for line in assembly_file:
        line = line.split()
        if line[0] == 'ORG':
            LC = int(line[1], 16)
            continue
        
        elif line[0] in mri_table:
            opcode = mri_table[line[0]] +  bin(int(sym_table[line[1]], 16))[2:].zfill(12)  # Adds the first bit that is fetched from MRI 
                                                                                        # table and adds it to the other 3 bits according to where the operand is located
        elif line[0] in non_mri_table:
            opcode = bin(int(non_mri_table[line[0]], 16))[2:].zfill(16)     # Translation to binary

        elif line[0] == 'DEC': 
            opcode = bin(0xFFFF & int(line[1]))[2:].zfill(16)

        elif line[0] == 'HEX':
            opcode = bin(0xFFFF & int(line[1], 16))[2:].zfill(16)


        elif line[0].endswith(','):
            if line[1] in mri_table:
                opcode = mri_table[line[1]] +  bin(int(sym_table[line[2]], 16))[2:].zfill(12)
        
            elif line[1] in non_mri_table:
                opcode = bin(int(non_mri_table[line[1]], 16))[2:].zfill(16)

            elif line[1] == 'DEC': 
                opcode = bin(0xFFFF & int(line[2]))[2:].zfill(16)

            elif line[1] == 'HEX':
                opcode = bin(0xFFFF & int(line[2], 16))[2:].zfill(16)

        elif line[0] == 'END':
            break

        machine_code[f"{bin(LC)[2:].zfill(12)}"] = opcode
        LC += 1

print(machine_code)


output_filename = "Machine_Code.txt"

with open(output_filename, "w") as output_file:
    for address, code in machine_code.items():
        output_file.write(f"{address}: {code}\n")

print(f"Machine code has been written to {output_filename}")
