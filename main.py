import serial
from p1_cmd_x06 import p1_cmd_x06_reply, p1_cmd_x06_send
from crc_16 import calculate_crc16
import log_config
import logging

# Configure logging by calling the function from log_config
log_config.configure_logging()


class P1CommandHandler:
    def __init__(self, address):
        self.address = address
        self.p1_packet = None  # Initialize as None
        self.logger = logging.getLogger(__name__)

    def construct_p1_packet(self, command_code, data=b''):
        sync_char = b'\x16'
        address_char = self.address.to_bytes(1, 'big')
        command_char = command_code.to_bytes(1, 'big')

        # Calculate total packet length
        total_length = len(sync_char) + 1 + len(address_char) + len(command_char) + len(data)

        # Calculate count_char
        count_char = total_length

        # Create the data to be passed to calculate_crc16
        crc_data = sync_char + count_char.to_bytes(1, 'big') + address_char + command_char + data

        # Calculate CRC
        crc = calculate_crc16(crc_data)

        # Construct the P1 packet
        self.p1_packet = sync_char + count_char.to_bytes(1,
                                                         'big') + address_char + command_char + data + crc.to_bytes(
            2, 'little')

        return self.p1_packet

    def send_p1_command(self, command_code, data=b'', response_size=256):
        self.construct_p1_packet(command_code, data)
        self.log_sent_p1_command()  # Log the sent P1 command

        # Configure serial port (adjust port and baud rate based on your setup)
        # with serial.Serial(port='/dev/ttyUSB0', baudrate=4800, timeout=1) as ser:
        with serial.Serial(port='COM6', baudrate=4800, timeout=1) as ser:
            # Send the P1 command
            ser.write(self.p1_packet)

            # Read the ser_response
            ser_response = ser.read(response_size)

        return ser_response

    def decode_read_point_response(self, response):

        if len(response) == 6 and response[3:5] == b'\x15\xF9':
            self.log_raw_response(response)  # Log the raw response
            return "NAK: Point does not exist. Error code F9."
        elif len(response) == 6 and response[3:5] == b'\x15\xF8':
            self.log_raw_response(response)  # Log the raw response
            return "NAK: Point is failed. Error code F8."
        elif len(response) == 8 and response[3:4] == b'\x06':
            value_decimal = int.from_bytes(response[4:6], 'little')
            end_result = 0.25 * value_decimal + 48
            self.logger.debug(f"Raw Response: {response.hex().upper()}\n"
                              f"                                  ACK: Point exists. Scaled Value: {end_result:.2f}")
            # Show packet details
            if Show_Packet_Details:
                p1_cmd_x06_reply(str(response.hex().upper()))

        elif len(response) == 6 and response[3:5] == b'\x15\xA9':
            self.log_raw_response(response)  # Log the raw response
            return "NAK: EEPROM is busy. Error code A9."
        else:
            self.log_raw_response(response)  # Log the raw response
            return "Invalid response."

    def send_get_point_info_command(self, report_number, format_byte):
        # Send the "Get Point Information (0AH)" command and read the response
        data = bytes([report_number, format_byte])
        response = self.send_p1_command(0x0A, data)
        self.decode_get_point_info_response(response)

    def decode_get_point_info_response(self, response):
        # Decode the response for "Get Point Information (0AH)" command
        # Implement the decoding logic based on the response format provided in your documentation
        # ...

        # Log the raw response
        self.log_raw_response(response)

    def log_sent_p1_command(self):
        self.logger.debug(f"Sent P1 Command: {self.p1_packet.hex().upper()}")

        # Show packet details
        if Show_Packet_Details:
            p1_cmd_x06_send(str(self.p1_packet.hex().upper()))

    def log_raw_response(self, response):
        self.logger.debug(f"Raw Response: {response.hex().upper()}")


# Example usage:
# Assume Show_Packet_Details is defined elsewhere
Show_Packet_Details = True
command_handler = P1CommandHandler(0x63)  # Controller Address 0x63 = 99, all controllers
response = command_handler.send_p1_command(0x06, b'\x04')  # Example: Read A Point from subpoint 0x02
decoded_response = command_handler.decode_read_point_response(response)

# Send the "Get Point Information (0AH)" command
command_handler.send_get_point_info_command(report_number=1, format_byte=0b00010001)
