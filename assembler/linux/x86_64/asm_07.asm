;
; asm_07.asm
;
; x86-64 Assembly
; Ubuntu Linux
;

      %include    "syscalls.inc"

      section     .data

      bMask       db      0x0f
      bAsciiDig   db      0x30
      bAsciiAlp   db      0x40

      dNum        dd      0x2468acef

      result      db      0x20,0x20
                  db      0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20
                  db      0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20
      resEnd      db      LF

      bAsciiHex   db      '0','1','2','3','4','5','6','7'
                  db      '8','9','a','b','c','d','e','f'

      section     .text

      global      main

main:

      ; get the number to convert
      mov       r8d, dword [dNum]
      
      ; get the number of nibbles
      mov       r10, 8
      
      ; start at the end of the string and work backwards
      mov       r11, resEnd-1

hex_loop:

      ; convert each nibble
      mov       r9, 0
      mov       r9b, r8b
      and       r9b, byte [bMask]
      add       r9, bAsciiHex
      mov       r9b, byte[r9]
      mov       byte [r11], r9b

      ; decrement the pointer
      dec       r11

      ; rotate in the next nibble
      ror       r8d, 4

      dec       r10
      cmp       r10, 0
      jne       hex_loop

      ; add the 0x to the front end
      mov       byte [r11], 'x'
      dec       r11
      mov       byte [r11], '0'

      ; write the string to STDOUT
      mov       rax, SYS_write
      mov       rdi, STDOUT
      mov       rsi, r11
      mov       rdx, resEnd+1
      sub       rdx, r11
      syscall

      mov       rax, SYS_exit
      mov       rdi, EXIT_SUCCESS
      syscall

