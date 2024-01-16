PRG    := cleanFile_UTF16  
CFLAGS := -Wall -g
C      := $(wildcard *.c)
OBJ    := ${C:.c=.o}

$(info ###################################)
$(info PRG    is $(PRG))
$(info CFLAGS is $(CFLAGS))
$(info C      is $(C))
$(info OBJ    is $(OBJ))
$(info ###################################)

all: clean link

clean:
	rm -f *.o $(PRG) 

%.o : %.c
	gcc $(CFLAGS) -c  $< -o $@ 

link: $(OBJ)
	gcc $(CFLAGS) $(OBJ) -o $(PRG)
	