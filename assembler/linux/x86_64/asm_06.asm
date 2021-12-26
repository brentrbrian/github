;
; asm_06.asm
;
; x86-64 Assembly
; Ubuntu Linux
;

      %include    "syscalls.inc"

      section     .data

      bMask       db      0x0f
      bAscii      db      0x30

      dNum        dd      0x12345678

      result      db      0x20,0x20
                  db      0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20
                  db      0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20
      resEnd      db      LF


      section     .text

      global      main

main:

      mov       r8d, dword [dNum]
      mov       r10, 8
      mov       r11, resEnd-1

shift_loop:

      mov       r9b, r8b
      and       r9b, byte [bMask]
      or        r9b, byte [bAscii]
      mov       byte [r11], r9b
      dec       r11

      ror       r8d, 4

      dec       r10
      cmp       r10, 0
      jne       shift_loop

      mov       byte [r11], 'x'
      dec       r11
      mov       byte [r11], '0'

      mov       rax, SYS_write
      mov       rdi, STDOUT
      mov       rsi, r11
      mov       rdx, resEnd+1
      sub       rdx, r11
      syscall

      mov       rax, SYS_exit
      mov       rdi, EXIT_SUCCESS
      syscall

