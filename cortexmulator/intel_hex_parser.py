import sys
from cortexmulator.mem0ry import Mem0ry


''' Class responsible of reading Intel Hex files and returning it as Mem0ry object '''
class HexParser:

    def __init__(self):
        self._memory = Mem0ry()

    def _check_line(self, line):
        '''
        Checks if line is correct by calculating checksum and comparing it to provided one
        :param line: String containing one line of hex file
        :return: True if line is correct, False in case of error
        '''
        if not line[0] == ':':
            return False
        _checksum = line[-3:-1]
        _checksum = hex(int(_checksum, 16))
        line = line[1:-3]
        _split_line = [int(line[i:i+2], 16) for i in range(0, len(line), 2)]
        _calculated_checksum = 0
        for item in _split_line:
            _calculated_checksum += item
        _calculated_checksum &= 0xff
        if not _calculated_checksum == 0x0:
            _calculated_checksum = 256 - _calculated_checksum
        else:
            _calculated_checksum = 0x0
        _calculated_checksum = hex(_calculated_checksum)
        if _checksum == _calculated_checksum:
            return True
        else:
            return False
        
    def hex_parser(self, file_path):
        '''
        Reads input hex file, checks if every line is correct and saves it as Mem0ry object
        :param file_path: Path to the hex file
        :return: Mem0ry object 
        '''
        with open(file_path) as hex_data:
            for line_counter, line in enumerate(hex_data):
                if self._check_line(line):
                    # here write to memory line by line
                    line = line[1:-3]
                    size = int(line[:2], 16)
                    address = int(line[2:6], 16)
                    record_type = int(line[6:8], 16)
                    if size > 0:
                        data = hex(int(line[8:], 16))
                        self._memory.write_memory(address, data, size)
                else:
                    print(f"Error in line {line_counter}\n {line}")
        
        return self._memory
