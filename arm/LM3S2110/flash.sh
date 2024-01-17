(
echo "open 127.0.0.1 4444"
sleep 1
echo "halt"
sleep 1
echo "flash write_image erase blinky.bin 0"
sleep 1
echo "exit"
sleep 1
) | telnet

exit 0;
