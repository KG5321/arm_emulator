from cortexmulator.intel_hex_parser import HexParser
from cortexmulator.mem0ry import Mem0ry
from bitstring import BitArray


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
            # print(f"instr: {bin(instruction)}")

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
                    rd = (instruction & 0x700) >> 8
                    imm8 = instruction & 0xFF
                    self.memory.write_register(f'r{rd}', imm8)
                    print(f"MOV r{rd} {imm8}")
                
                if instruction & 0x3800 == 0x2800:
                    print("CMP (immediate)")

                if instruction & 0x3800 == 0x3000:
                    imm8 = instruction & 0xFF
                    rdn = (instruction & 0x700) >> 8
                    rdn_val = self.memory.read_register(f'r{rdn}')
                    result = imm8 + rdn_val
                    self.memory.write_register(f'r{rdn}', result)
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
                    rd = instruction & 0x7
                    rm = (instruction & 0x78) >> 3
                    d = instruction & 0x80 >> 4
                    rd += d
                    self.memory.write_register(f'r{rd}', self.memory.read_register(f'r{rm}'))
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
                        rt = instruction & 0x7
                        rn = (instruction & 0x38) >> 3
                        imm5 = (instruction & 0x7C0) >> 6
                        offset_addr = self.memory.read_register(f'r{rn}') + imm5 + self.memory._start_addr
                        data = str(hex(self.memory.read_register(f'r{rt}')))[2:]
                        data_len = len(data)
                        self.memory.write_memory(offset_addr, data, data_len)
                        print("STR (immediate)")
                    
                    if instruction & 0x800 == 0x800:
                        rt = instruction & 0x7
                        rn = (instruction & 0x38) >> 3
                        imm5 = (instruction & 0x7C0) >> 6
                        offset_addr = self.memory.read_register(f'r{rn}') + imm5 + self.memory._start_addr
                        self.memory.write_register(f'r{rt}', int(self.memory.read_memory(offset_addr, 2)))
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
                rd = instruction & 0x700
                rd = rd >> 8
                imm8 = instruction & 0xFF
                sp_val = self.memory.read_register('r13')
                sp_val += imm8
                self.memory.write_register(f'r{rd}',sp_val)
                print(f"ADD r{rd} sp #{imm8}")
            
            if instruction & 0xF000 == 0xB000:
                
                if instruction & 0xF80 == 0:
                    print("ADD (SP plus immediate)")
                    
                if instruction & 0xF80 == 0x80:
                    print(bin(instruction))
                    imm7 = instruction & 0x7F
                    imm32 = self.zero_extend(imm7)
                    imm32 = str(bin(0xFFFFFFFF - int(imm32, 2)))[2:]
                    print(imm32)
                    int_imm32 = BitArray(bin=imm32).int
                    print(int_imm32)
                    
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
                    imm8 = instruction & 0xFF
                    registers = str(bin(imm8))[2:]
                    register_list = []
                    for idx, i in enumerate(registers[::-1]):
                        if i == '1':
                            register_list.append(f"r{idx}")
                            reg_val = self.memory.read_register(f'r{idx}')
                            self.memory.push_to_stack(reg_val)
                    m = instruction & 0x100
                    m = m >> 8
                    lr = False
                    if m == 1:
                        register_list.append('lr')
                        lr_val = self.memory.read_register('r14')
                        self.memory.push_to_stack(lr_val)
                    print(f"PUSH {register_list}")
                    
                    
                
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
                    print(bin(instruction))

                if instruction & 0xF00 == 0xE00:
                    print("UDF")
                
                if instruction & 0xF00 == 0xF00:
                    print("SVC")

            if instruction & 0xF800 == 0xE000:
                imm11 = instruction & 0x7FF
                imm32 = self.sign_extend(imm11)
                int_imm32 = BitArray(bin=imm32).int
                current_pc = self.memory.pc()
                new_pc = current_pc + int_imm32
                self.memory.set_pc(new_pc)
                print(f"B {hex(new_pc)}")
            
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
    
    def zero_extend(self, imm):
        imm_ext_len = 32 - len(str(bin(imm))[2:])
        imm32 = ""
        for i in range(imm_ext_len):
            imm32 += '0'
        imm32 += str(bin(imm))[2:]
        return imm32

    def sign_extend(self, imm):
        imm_ext_len = 32 - len(str(bin(imm))[2:])
        imm32 = ""
        for i in range(imm_ext_len):
            imm32 += '1'
        imm32 += str(bin(imm))[2:]
        return imm32
