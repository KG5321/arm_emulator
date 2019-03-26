class Mem0ry:
    
    def __init__(self):
        self._memory = [None] * 65535
        # General purpose registers
        self._r0 = 0x0000
        self._r1 = 0x0000
        self._r2 = 0x0000
        self._r3 = 0x0000
        self._r4 = 0x0000
        self._r5 = 0x0000
        self._r6 = 0x0000
        self._r7 = 0x0000
        self._r8 = 0x0000
        self._r9 = 0x0000
        self._r10 = 0x0000
        self._r11 = 0x0000
        self._r12 = 0x0000
        # Special registers
        self._r13 = 0x0000 # Stack pointer
        self._r14 = 0x0000 # Link register
        self._r15 = 0x0000 # Program counter
        self._psr = 0x0000 # Program status register
        self._primask = 0x0000
        self._control = 0x0000
        self._registers = {'r0': self._r0,
                     'r1': self._r1,
                     'r2': self._r2,
                     'r3': self._r3,
                     'r4': self._r4,
                     'r5': self._r5,
                     'r6': self._r6,
                     'r7': self._r7,
                     'r8': self._r8,
                     'r9': self._r9,
                     'r10': self._r10,
                     'r11': self._r11,
                     'r12': self._r12,
                     'r13': self._r13,
                     'r14': self._r14,
                     'r15': self._r15,
                     'psr': self._psr,
                     'primask': self._primask,
                     'control': self._control}

    def read_memory(self, address, size):
        last_byte = address + size
        data = self._memory[address]
        byte_counter = 1
        while address+byte_counter < last_byte:
            if self._memory[address+byte_counter] is not None:
                data += str(self._memory[address+byte_counter])
                byte_counter += 1
            else: return data
        return data

    def write_memory(self, address, data, size):
        current_address = address + size - 1
        if 'x' not in data[-2:]:
            self._memory[current_address] = data[-2:]
        else:
            self._memory[current_address] = '00'
        counter = -2
        while current_address > address:
            counter -= 2
            if data[counter:counter+2] != '0x':
                current_address -= 1
                if data[counter:counter+2] != '' and len(data[counter:counter+2]) == 2:
                    if 'x' in data[counter:counter+2]:
                        tmp = data[counter:counter+2]
                        tmp = tmp.replace('x', '0')
                        self._memory[current_address] = tmp
                    else:
                        self._memory[current_address] = data[counter:counter+2]
                else:
                    self._memory[current_address] = '00'

    
    def read_register(self, register):
        return self._registers[register]
    
    def write_register(self, register, data):
        self._registers[register] = data

    def pc(self):
        return self._r15
    
    def inc_pc(self):
        self._r15 += 2