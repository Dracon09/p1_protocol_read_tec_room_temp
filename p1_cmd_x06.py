def p1_cmd_x06_send(hexstring):
    # Convert hex string to a list of integers
    data = [int(hexstring[i:i + 2], 16) for i in range(0, len(hexstring), 2)]

    # Convert each value to a formatted string with right alignment
    formatted_values = [f"0x{value:02X}" for value in data]
    fln_address = f"{int(formatted_values[2], 16):02d}"
    sub_point_num = f"{int(formatted_values[4], 16):03d}"

    # Create a box-drawing style table
    print(f"""+-------+-------+-------+-------+-------+---------+
| {formatted_values[0]}  | {formatted_values[1]}  |  {fln_address}   | {formatted_values[3]}  |  {sub_point_num}  | {formatted_values[-2]}{formatted_values[-1][2:]}  | Read A Point (06H) Command
+-------+-------+-------+-------+-------+---------+
    |       |       |        |       |       |
    |       |       |        |       |       +---- CRC-16 
    |       |       |        |       +------------ Subpoint Number
    |       |       |        +-------------------- P1 Command
    |       |       +----------------------------- FLN Controller Address
    |       +------------------------------------- Packet total length count -2
    +--------------------------------------------- P1 Sync Character (Always 0x16)""")

# Example usage:
# hexstring = "1605630604BB72"
# formatted_output = format_hex_string(hexstring)
# print(formatted_output)


def p1_cmd_x06_reply(hexstring):
    # Convert hex string to a list of integers
    data = [int(hexstring[i:i + 2], 16) for i in range(0, len(hexstring), 2)]

    # Convert each value to a formatted string with right alignment
    formatted_values = [f"0x{value:02X}" for value in data]
    fln_address = f"{int(formatted_values[2], 16):02d}"
    sub_point_value = f"{0.25 * int(formatted_values[4], 16) + 48:07.2f}"

    # Create a box-drawing style table
    print(f"""+-------+-------+-------+-------+-----------+---------+
| {formatted_values[0]}  | {formatted_values[1]}  |  {fln_address}   | {formatted_values[3]}  |   {sub_point_value}   | {formatted_values[-2]}{formatted_values[-1][2:]}  | Read A Point (06H) Response
+-------+-------+-------+-------+-----------+---------+
    |       |       |        |       |         |
    |       |       |        |       |         +-- CRC-16 
    |       |       |        |       +------------ Scaled Point Value
    |       |       |        +-------------------- Acknowlege ACK (0x06)
    |       |       +----------------------------- FLN Controller Address
    |       +------------------------------------- Packet total length count -2
    +--------------------------------------------- P1 Sync Character (Always 0x16)""")

# Example usage:
# hexstring = "1605630604BB72"
# formatted_output = format_hex_string(hexstring)
# print(formatted_output)
