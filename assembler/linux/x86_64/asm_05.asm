;
; asm_05.asm
;
; x86-64 Assembly
; Ubuntu Linux
;

      %include    "syscalls.inc"

      section     .data

      bMask       db      0x0f
      bAscii      db      0x30
      bNum        db      0

      dNum        dd      0x12345678

      result      dw      '0x'
      hexq        dq      0
                  db      LF
      resLen      equ     $-result

      msg:        db      '0x'
      msglen:     equ     $-msg

      section     .text

      global      main

main:

      mov       r8d, dword [dNum]
      mov       r10, 8

shift_loop:

      shl       r9, 8

      mov       r9b, r8b
      and       r9b, byte [bMask]
      or        r9b, byte [bAscii]

      ror       r8d, 4

      dec       r10
      cmp       r10, 0
      jne       shift_loop

      mov       qword [hexq], r9


      mov       rax, SYS_write
      mov       rdi, STDOUT
      mov       rsi, result
      mov       rdx, resLen
      syscall

      mov       rax, SYS_exit
      mov       rdi, EXIT_SUCCESS
      syscall
