from cortexmulator.cortexm0lator import CortexM0lator


m = CortexM0lator()
m.read_hex_data('/Users/Konrad/Developer/Python/arm_emulator/c_files/a.hex')

# print(m.read_memory(0x0000))
# print(m.read_register('r10'))
# m.memory.write_register('r10', 0xfafa)
# print(hex(m.read_register('r10')))
m.run()
# print(m.memory._memory)