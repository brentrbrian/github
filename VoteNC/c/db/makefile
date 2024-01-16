
INCS    := $(shell mariadb_config --include)
LIBS    := $(shell mariadb_config --libs)

CFLAGS  := -Wall -g $(INCS)
LFLAGS  := $(LIBS)

C       := $(wildcard *.c)

DB_C    := $(wildcard db_*.c)
DB_O    := ${DB_C:.c=.o}

MOD_C   := $(filter-out $(DB_C), $(C))
MOD_O   := ${MOD_C:.c=.o}

BIN     := $(basename $(DB_C))

$(info ###################################)
$(info INCS   | $(INCS))
$(info LIBS   | $(LIBS))
$(info CFLAGS | $(CFLAGS))
$(info LFLAGS | $(LFLAGS))
$(info C      | $(C))
$(info DB_C   | $(DB_C))
$(info DB_O   | $(DB_O))
$(info MOD_C  | $(MOD_C))
$(info MOD_O  | $(MOD_O))
$(info BIN    | $(BIN))
$(info ###################################)


all: clean objects binary

clean:
	rm -f *.o *.bin $(BIN)

%.o : %.c
	gcc $(CFLAGS) -c $< -o $@
	
objects: $(MOD_O) $(DB_O)

% : %.o
	gcc $<  $(MOD_O) $(LFLAGS)  -o $@

binary: $(BIN)

