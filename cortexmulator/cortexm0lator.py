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
        while self._is_cpu_running:
            
            instr = self.read_memory(self.memory.pc())
            
            if instr is None:
                self._is_cpu_running = False
                break
            
            instruction = int(instr, 16)
            # print(f"PC: {hex(self.memory.pc())}")
            # print(f"instr: {hex(instruction)}")

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

                if instruction & 0x3C0 == 0:
                    print("AND (register)")

                if instruction & 0x3C0 == 0x40:
                    print("EOR (register")
                
                if instruction & 0x3C0 == 0x80:
                    print("LSL (register)")

                if instruction & 0x3C0 == 0xC0:
                    print("LSR (register)")

                if instruction & 0x3C0 == 0x100:
                    print("ASR (register)")
                
                if instruction & 0x3C0 == 0x140:
                    print("ADC (register)")

                if instruction & 0x3C0 == 0x180:
                    print("SBC (register)")

                if instruction & 0x3C0 == 0x1C0:
                    print("ROR (register)")

                if instruction & 0x3C0 == 0x200:
                    print("TST (register)")
                
                if instruction & 0x3C0 == 0x240:
                    print("RSB (immediate)")
                
                if instruction & 0x3C0 == 0x280:
                    print("CMP (register)")

                if instruction & 0x3C0 == 0x2C0:
                    print("CMN (register)")

                if instruction & 0x3C0 == 0x300:
                    print("ORR (register)")

                if instruction & 0x3C0 == 0x340:
                    print("MUL")
                
                if instruction & 0x3C0 == 0x380:
                    print("BIC (register)")
                
                if instruction & 0x3C0 == 0x3C0:
                    print("MVN (register)")

            if instruction & 0xFC00 == 0x4400:
                
                if instruction & 0x300 == 0:
                    print("ADD (register)")
                
                if instruction & 0x3C0 == 0x100:
                    print("UNPREDICTABLE")

                if instruction & 0x3C0 == 0x140 or instruction & 0x380 == 0x180:
                    print("CMP (register)")

                if instruction & 0x300 == 0x200:
                    print("MOV (register)")
                
                if instruction & 0x380 == 0x300:
                    print("BX")

                if instruction & 0x380 == 0x380:
                    print("BLX (register)")

            if instruction & 0xF800 == 0x4800:
                print("LDR (literal)")
            
            if instruction & 0xF000 == 0x5000 or instruction & 0xE000 == 0x6000 or instruction & 0xE000 == 0x8000:
                if instruction & 0xF000 == 0x5000:
                    if instruction & 0xE00 == 0:
                        print("STR (register)")
                    
                    if instruction & 0xE00 == 0x200:
                        print("STRH (register)")

                    if instruction & 0xE00 == 0x400:
                        print("STRB (register)")

                    if instruction & 0xE00 == 0x600:
                        print("LDRSB (register)")

                    if instruction & 0xE00 == 0x800:
                        print("LDR (register)")

                    if instruction & 0xE00 == 0xA00:
                        print("LDRH (register)")

                    if instruction & 0xE00 == 0xC00:
                        print("LDRB (register")

                    if instruction & 0xE00 == 0xE00:
                        print("LDRSH (register)")

                if instruction & 0xF000 == 0x6000:
                    if instruction & 0x800 == 0:
                        print("STR (immediate)")
                    
                    if instruction & 0x800 == 0x800:
                        print("LDR (immediate)")

                if instruction & 0xF000 == 0x7000:
                    if instruction & 0x800 == 0:
                        print("STRB (immediate)")
                    
                    if instruction & 0x800 == 0x800:
                        print("LDRB (immediate)")

                if instruction & 0xF000 == 0x8000:
                    if instruction & 0x800 == 0:
                        print("STRH (immediate)")
                    
                    if instruction & 0x800 == 0x800:
                        print("LDRH (immediate)")

                if instruction & 0xF000 == 0x9000:
                    if instruction & 0x800 == 0:
                        print("STR (immediate)")
                    
                    if instruction & 0x800 == 0x800:
                        print("LDR (immediate)")

            if instruction & 0xF800 == 0xA000:
                print("ADR")

            if instruction & 0xF800 == 0xA800:
                print("ADD (SP plus immediate)")
                # print(bin(instruction))
                rd = instruction & 0x700
                rd = rd >> 8
                imm8 = instruction & 0xFF
                # print(f"ADD r{rd} sp #{imm8}")
            
            if instruction & 0xF000 == 0xB000:
                
                if instruction & 0xF80 == 0:
                    print("ADD (SP plus immediate)")
                    
                if instruction & 0xF80 == 0x80:
                    print("SUB (SP minus immediate)")

                if instruction & 0xFC0 == 0x200:
                    print("SXTH")

                if instruction & 0xFC0 == 0x240:
                    print("SXTB")
                
                if instruction & 0xFC0 == 0x280:
                    print("UXTH")
                
                if instruction & 0xFC0 == 0x2C0:
                    print("UXTB")

                if instruction & 0xE00 == 0x400:
                    print("PUSH")
                    # print(bin(instruction))
                    imm8 = instruction & 0xFF
                    imm8 = imm8 >> 8
                    m = instruction & 0x100
                    m = m >> 8

                    # a = 0b0100 0000 0000 0000
                    
                    
                
                if instruction & 0xFE0 == 0x660:
                    print("CPS")
                
                if instruction & 0xFC0 == 0xA00:
                    print("REV")
                
                if instruction & 0xFC0 == 0xA40:
                    print("REV16")
                
                if instruction & 0xFC0 == 0xAC0:
                    print("REVSH")

                if instruction & 0xE00 == 0xC00:
                    print("POP")

                if instruction & 0xF00 == 0xE00:
                    print("BKPT")

                if instruction & 0xF00 == 0xF00:
                    if instruction & 0xFF == 0:
                        print("NOP")
                    
                    if instruction & 0xFF == 0x10:
                        print("YIELD")
                    
                    if instruction & 0xFF == 0x20:
                        print("WFE")

                    if instruction & 0xFF == 0x30:
                        print("WFI")

                    if instruction & 0xFF == 0x40:
                        print("SEV")

            if instruction & 0xF800 == 0xC000:
                print("STM, STMIA, STMEA")
            
            if instruction & 0xF800 == 0xC800:
                print("LDM, LDMIA, LDMFD")
            
            if instruction & 0xF000 == 0xD000:
                if instruction & 0xE00 != 0xE00:
                    print("B")

                if instruction & 0xF00 == 0xE00:
                    print("UDF")
                
                if instruction & 0xF00 == 0xF00:
                    print("SVC")

            if instruction & 0xF800 == 0xE000:
                print("B")
            
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
