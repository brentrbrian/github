SRC        = $(wildcard *.asm)
OBJ        = ${SRC:.asm=}

all: $(OBJ)

clean:
	rm -rf $(OBJ)

% : %.asm

	yasm -g dwarf2  -f elf64 $< -o $@.o -l $@.lst
	gcc  -g -no-pie             -o $@  $@.o

push:

	git commit -m "add new programs"
	git push
