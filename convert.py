def hex_to_twos_complement(hex_num):
    # Convert hex to decimal integer
    num = int(hex_num, 16)

    bits = len(hex_num) * 4  # Each hex digit represents 4 bits

    # Compute the 2's complement for negative values
    if num & (1 << (bits - 1)):  # Check if it's a negative number in 2's complement
        num = num - (1 << bits)  # Subtract 2^bits to get the negative decimal value

    # Convert to binary, padding to the full bit length
    binary_representation = f"{num & ((1 << bits) - 1):0{bits}b}"

    # Format the binary output with spaces every 4 bits
    binary_with_spaces = ' '.join(binary_representation[i:i+4] for i in range(0, len(binary_representation), 4))

    return num, binary_with_spaces

hex_num = input("Enter a hexadecimal number (e.g., FFFF): ")
twos_complement_decimal, twos_complement_binary = hex_to_twos_complement(hex_num)

print(f"The 2's complement of hex {hex_num} is:")
print(f"Decimal: {twos_complement_decimal}")
print(f"Binary: {twos_complement_binary}")