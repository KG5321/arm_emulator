b.hex: b.elf
	arm-none-eabi-objcopy -O ihex b.elf b.hex

b.elf: b.o
	arm-none-eabi-ld -Ttext 0x8000000 b.o -o b.elf

b.o: b.s
	arm-none-eabi-as -mthumb -o b.o b.s

b.s: b.c
	arm-none-eabi-gcc -S -mcpu=cortex-m0 -O0 -mthumb b.c
