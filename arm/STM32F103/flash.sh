(
echo "open 127.0.0.1 4444"
sleep 1
echo "reset halt"
sleep 1
echo "flash probe 0"
sleep 1
echo "stm32f1x mass_erase 0"
sleep 1
echo "flash write_bank 0 blinky.bin 0"
sleep 1
echo "reset run"
sleep 1
echo "exit"
sleep 1
) | telnet

exit 0;

