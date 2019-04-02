from cortexmulator.intel_hex_parser import HexParser
from cortexmulator.mem0ry import Mem0ry


''' Main ARM Cortex-M0 emulation class '''
class CortexM0lator:

    def __init__(self):
        self._is_cpu_running = False
        self._cpu_cycle_counter = None
        self.memory = Mem0ry()
        self.parser = HexParser()
    
    def read_hex_data(self, file_name):
        ''' Reads hex file and saves as Mem0ry object '''
        self.memory = self.parser.hex_parser(file_name)
    
    def run(self):
        ''' Method responsible of starting emulation '''
        self._is_cpu_running = True
        self._cpu_loop()
        self._is_cpu_running = False

    def _cpu_loop(self):
        ''' Main cpu loop '''
        while self._is_cpu_running and self.memory.pc() < 65534:
            instruction = self.read_memory(self.memory.pc())

            # decoder
            if instruction is not None: # temporary 
                print(hex(self.memory.pc()), bin(int(instruction, 16))[2:].zfill(16))

            self.memory.inc_pc()

    def read_memory(self, address):
        ''' Method responsible of reading memory in given addres '''
        data = self.memory.read_memory(address, 2)
        return data

    def read_register(self, register):
        return self.memory.read_register(register)

    def check_cpu_status(self):
        ''' Method returns current cpu state '''
        if self._is_cpu_running:
            return 'Running'
        return 'Not running'
