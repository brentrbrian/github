SRC        = $(wildcard *.c)
OBJ        = ${SRC:.c=}

#
CFLAGS     := -g -O0 -Wall -I. 

all: $(OBJ)

clean:
	rm -rf $(OBJ)

% : %.c
	aarch64-linux-gnu-gcc $(CFLAGS)  $< -o $@ 
