SRC        = $(wildcard *.rs)
OBJ        = ${SRC:.rs=}

all: $(OBJ)

clean:
	rm -rf $(OBJ)

% : %.rs
	rustc $< -o $@ 
