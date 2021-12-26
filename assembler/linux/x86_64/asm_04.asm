;
; asm_04.asm
;
; x86-64 Assembly Language Programming with Ubuntu 
;
; Ed Jorgensen, Ph.D.
; Version 1.1.40
; January 2020
;

      %include    "syscalls.inc"

      section     .data

      msg:        db      'hello world',LF

      msglen:     equ     $-msg

      section     .text

      global main

main:

      mov       rax, SYS_write
      mov       rdi, STDOUT
      mov       rsi, msg
      mov       rdx, msglen
      syscall

      mov       rax, SYS_exit
      mov       rdi, EXIT_SUCCESS
      syscall

