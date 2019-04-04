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
            
            instr = self.read_memory(self.memory.pc())
            
            if instr is None:
                self._is_cpu_running = False
                break
            
            instruction = int(instr, 16)

            if instruction & 0xC000 == 0:
                if instruction & 0x3800 == 0:
                    if instruction & 0x7C0 == 0:
                        print("MOV (register)")
                    else:
                        print("LSL (immediate)")
                
                if instruction & 0x3800 == 0x0800:
                    print("LSR (immediate)")

                if instruction & 0x3800 == 0x1000:
                    print("ASR (immediate)")

                if instruction & 0x3E00 == 0x1800:
                    print("ADD (register)")

                if instruction & 0x3E00 == 0x1A00:
                    print("SUB (register)")
                
                if instruction & 0x3E00 == 0x1C00:
                    print("ADD (immediate)")

                if instruction & 0x3E00 == 0x1E00:
                    print("SUB (immediate)")

                if instruction & 0x3800 == 0x2000:
                    print("MOV (immediate)")
                
                if instruction & 0x3800 == 0x2800:
                    print("CMP (immediate)")

                if instruction & 0x3800 == 0x3000:
                    print("ADD 8-bit (immediate)")
                
                if instruction & 0x3800 == 0x3800:
                    print("SUB 8-bit (immediate)")


            if instruction & 0xFC00 == 0x4000:
                print("data processing")

            if instruction & 0xFC00 == 0x4400:
                print("special data instr")
            
            if instruction & 0xF800 == 0x4800:
                print("load from literal pool")
            
            if instruction & 0xF000 == 0x5000 or instruction & 0xE000 == 0x6000 or instruction & 0xE000 == 0x8000:
                print("load/store single data item")

            if instruction & 0xF800 == 0xA000:
                print("generate pc-relative address")

            if instruction & 0xF800 == 0xA800:
                print("generate sp-relative address")
            
            if instruction & 0xF000 == 0xB000:
                print("misc 16bit instr")
            
            if instruction & 0xF800 == 0xC000:
                print("store multiple registers")
            
            if instruction & 0xF800 == 0xC800:
                print("load multiple registers")
            
            if instruction & 0xF000 == 0xD000:
                print("conditional branch")

            if instruction & 0xF800 == 0xE000:
                print("unconditional branch")
            
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
