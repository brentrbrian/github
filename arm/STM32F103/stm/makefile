SRC        = $(wildcard *.c)
OBJ        = ${SRC:.c=.o}

ARM        = `cat arm_path`

CC         = $(ARM)/arm-none-eabi-gcc
OC         = $(ARM)/arm-none-eabi-objcopy
OD         = $(ARM)/arm-none-eabi-objdump

CFLAGS     := -g -O0 -mcpu=cortex-m3 -mthumb -fsigned-char -ffunction-sections -mlittle-endian -MD -Wcast-align -Wall
CFLAGS     += -I.

all: $(OBJ)

clean:
	rm -rf *.d *.o *.lst $(PRG).elf $(PRG).hex $(PRG).bin

%.o : %.c
	$(CC) -c $(CFLAGS) $< -o $@

