;
; asm_02.asm - add instruction
;
; x86-64 Assembly Language Programming with Ubuntu 
;
; Ed Jorgensen, Ph.D.
; Version 1.1.40
; January 2020
;

      %include    "syscalls.inc"
      %include    "macros.inc"
       
      section     .data
      
      bMask       db      0x0f

      result      db      0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20
                  db      0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20
                  db      0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20
                  db      0x20,0x20,LF,LF
      resEnd
      
      bAsciiHex   db      '0','1','2','3','4','5','6','7'
                  db      '8','9','a','b','c','d','e','f'      

      bVar1       db      17        ;      0x1a
      bVar2       db      9

      wVar1       dw      17000     ;    0x6590
      wVar2       dw      9000

      dVar1       dd      17000000  ; 0x18CBA80
      dVar2       dd      9000000

      qVar1       dq      170000000 ; 0xF7F4900
      qVar2       dq      90000000

      section     .text

      global      main
       
 main:
 
      mov       r8, 0
       
      mov       r8b, byte [bVar1]
      add       r8b, byte [bVar2]
      mov       r10, 2
      call      print_hex

      mov       r8w, word [wVar1]
      add       r8w, word [wVar2]
      mov       r10, 4
      call      print_hex      
      
      mov       r8d, dword [dVar1]
      add       r8d, dword [dVar2]
      mov       r10, 8
      call      print_hex      
      
      mov       r8, qword [qVar1]
      add       r8, qword [qVar2]
      mov       r10, 16
      call      print_hex
             
exit:
       
      mov       rax, SYS_exit
      mov       rdi, EXIT_SUCCESS
      syscall

;
; subroutines
;

print_hex:

      ; start at the end of the string and work backwards
      mov       r11, resEnd-3

hex_loop:

    
      ; convert each nibble
      mov       r9, 0
      mov       r9b, r8b
      and       r9b, byte [bMask]
      add       r9,  bAsciiHex
      mov       r9b, byte [r9]
      mov       byte [r11], r9b

      ; decrement the pointer
      dec       r11

      ; rotate in the next nibble
      ror       r8, 4

      dec       r10
      cmp       r10, 0
      jne       hex_loop

      ; add the LF 0x
      mov       byte [r11], 'x'
      dec       r11
      mov       byte [r11], '0'
      dec       r11
      mov       byte [r11], LF

      
      mov       rdx, resEnd-1
      sub       rdx, r11
      
      PRINT     r11, rdx
      
      ret
