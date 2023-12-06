def calculate_crc16(data):
    crc = 0x0000  # Initial seed value

    for byte in data:
        crc ^= byte  # XOR with the data byte

        for _ in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= 0xA001  # XOR with the polynomial
            else:
                crc >>= 1

    return crc & 0xFFFF

# Given test vector
# test_vector = bytes.fromhex("16 07 02 21 03 91 03")
# CRC-16: d81b

# Prompt the user for the test vector as a hex value
# test_vector_hex = input("Enter the test vector as a hex value (e.g., 1603070618): ")

# Convert the hex input to bytes
# test_vector = bytes.fromhex(test_vector_hex)

# Calculate CRC-16
# crc = calculate_crc16(test_vector)

# Correct the byte order
# crc_bytes = crc.to_bytes(2, 'big')
# crc_hex = crc_bytes[1:].hex() + crc_bytes[:1].hex()

# print(f"CRC-16: {crc_hex}")
# print(f"CRC-16: d81b")
