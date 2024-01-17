PRG        = blinky
SRC        = $(wildcard *.c)
OBJ        = ${SRC:.c=.o}
ARM        = `cat arm_path`

CC         = $(ARM)/arm-none-eabi-gcc
OC         = $(ARM)/arm-none-eabi-objcopy
OD         = $(ARM)/arm-none-eabi-objdump

CFLAGS     := -g -O0 -mcpu=cortex-m3 -mthumb -fsigned-char -ffunction-sections -mlittle-endian -MD -Wcast-align -Wall
CFLAGS     += -I.
CFLAGS     += -D_LM3S9D96_

LDFLAGS    =  -u _start -Wl,-static -Wl,--gc-sections -Wl,-Map -Xlinker $(PRG).map -Wl,-T -Xlinker $(PRG).ld -nostdlib -nostartfiles

ASFLAGS    = -Wa

all: clean elf hex bin

clean:
	rm -rf *~ core.* *.d *.o *.O *.lst $(PRG).elf $(PRG).hex $(PRG).bin

elf: $(OBJ)
	$(CC) $(OBJ) $(LIB) $(LDFLAGS) -o $(PRG).elf

hex:
	$(OC) -O ihex   $(PRG).elf $(PRG).hex

bin:
	$(OC) -O binary $(PRG).elf $(PRG).bin

flash: $(OBJ)
	bash flash.sh

%.O : %.s
	$(CC) -c $(ASFLAGS) $< -o $@

%.o : %.c
	$(CC) -c $(CFLAGS) $< -o $@

