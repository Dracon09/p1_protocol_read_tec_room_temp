# p1_protocol_read_tec_room_temp
test code as a proof of concept in talking to a TEC (terminal equipment controller) over rs-485 with the P1 Protocol

+-------+-------+-------+-------+-------+---------+
| 0x16  | 0x05  |  99   | 0x06  |  004  | 0xBB72  | Read A Point (06H) Command
+-------+-------+-------+-------+-------+---------+
    |       |       |        |       |       |
    |       |       |        |       |       +---- CRC-16 
    |       |       |        |       +------------ Subpoint Number
    |       |       |        +-------------------- P1 Command
    |       |       +----------------------------- FLN Controller Address
    |       +------------------------------------- Packet total length count -2
    +--------------------------------------------- P1 Sync Character (Always 0x16)
DEBUG - Sent P1 Command: 1605630604BB72
+-------+-------+-------+-------+-----------+---------+
| 0x16  | 0x06  |  99   | 0x06  |   0069.50   | 0x4B13  | Read A Point (06H) Response
+-------+-------+-------+-------+-----------+---------+
    |       |       |        |       |         |
    |       |       |        |       |         +-- CRC-16 
    |       |       |        |       +------------ Scaled Point Value
    |       |       |        +-------------------- Acknowlege ACK (0x06)
    |       |       +----------------------------- FLN Controller Address
    |       +------------------------------------- Packet total length count -2
    +--------------------------------------------- P1 Sync Character (Always 0x16)

DEBUG - Raw Response: 1606630656004B13
                      ACK: Point exists. Scaled Value: 69.50
