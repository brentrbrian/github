
all:

	@echo "***********"
	@echo "* STARTING "
	@echo "***********"

	$(MAKE) -C assembler/linux/x86_64
	$(MAKE) -C rust
	
	@echo "***********"
	@echo "* ENDING   "
	@echo "***********"