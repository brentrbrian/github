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

      bNumA       db      63
      bNumB       db      17
      bNumC       db      5
      bAns1       db      0
      bAns2       db      0
      bRem2       db      0
      bAns3       db      0

      wNumA       dw      4321
      wNumB       dw      1234
      wNumC       dw      167
      wAns1       dw      0
      wAns2       dw      0
      wRem2       dw      0
      wAns3       dw      0

      dNumA       dd      42000
      dNumB       dd      -3157
      dNumC       dd      -293
      dAns1       dd      0
      dAns2       dd      0
      dRem2       dd      0
      dAns3       dd      0

      qNumA       dq      730000
      qNumB       dq      -13456
      qNumC       dq      -1279
      qAns1       dq      0
      qAns2       dq      0
      qRem2       dq      0
      qAns3       dq      0

      section .text

      global main

main:

      ; bNumA       db      63
      ; bNumB       db      17
      ; bNumC       db      5

      mov       al, byte [bNumA] ; 63 / 3 = 21 = 0x15
      mov       ah, 0
      mov       bl, 3
      div       bl
      mov       byte [bAns1], al
      
      mov       r8,0
      mov       r8b, byte [bAns1]
      mov       r10, 2
      call      print_hex

      mov       al, byte [bNumA] ; 63 / 17 = 3 = 0x03
      div       byte [bNumB]
      mov       byte [bAns2], al
      mov       byte [bRem2], ah
      
      mov       r8,0
      mov       r8b, byte [bAns2]
      mov       r10, 2
      call      print_hex      

      mov       r8,0
      mov       r8b, byte [bRem2]
      mov       r10, 2
      call      print_hex 

      mov       al, byte [bNumA] ; 63 * 5 / 17 = 0x12
      mul       byte [bNumC]
      div       byte [bNumB]
      mov       byte [bAns3], al
      
      mov       r8,0
      mov       r8b, byte [bAns3]
      mov       r10, 2
      call      print_hex
      
      ; wNumA       dw      4321
      ; wNumB       dw      1234
      ; wNumC       dw      167      

      mov       ax, word [wNumA] ; 4321 / 5 = 864 = 0x360
      mov       dx, 0
      mov       bx, 5
      div       bx
      mov       word [wAns1], ax

      mov       r8,0
      mov       r8w, word [wAns1]
      mov       r10, 4
      call      print_hex

      mov       dx, 0
      mov       ax, word [wNumA] ; 4321 / 1234 = 3 rem 0x26b
      div       word [wNumB]
      mov       word [wAns2], ax
      mov       word [wRem2], dx
      
      mov       r8,0
      mov       r8w, word [wAns2]
      mov       r10, 4
      call      print_hex
      
      mov       r8,0
      mov       r8w, word [wRem2]
      mov       r10, 4
      call      print_hex

      mov       ax, word [wNumA] ; 4321 * 167 / 1234 = 584 = 0x248
      mul       word [wNumC]
      div       word [wNumB]
      mov       word [wAns3], ax
      
      mov       r8,0
      mov       r8w, word [wAns3]
      mov       r10, 4
      call      print_hex

      ; dNumA       dd      42000
      ; dNumB       dd      -3157
      ; dNumC       dd      -293
      
      mov       eax, dword [dNumA] ; 42000 / 7 = 6000 = 0x1770
      cdq
      mov       ebx, 7
      idiv      ebx
      mov       dword [dAns1], eax
      
      mov       r8,0
      mov       r8d, dword [dAns1]
      mov       r10, 8
      call      print_hex   

      mov       eax, dword [dNumA] ; 42000 / -3157 = 13 rem 960 = 0x3bf
      cdq
      idiv      dword [dNumB]
      mov       dword [dAns2], eax
      mov       dword [dRem2], edx
      
      mov       r8,0
      mov       r8d, dword [dAns2]
      mov       r10, 8
      call      print_hex   
      
      mov       r8,0
      mov       r8d, dword [dRem2]
      mov       r10, 8
      call      print_hex   

      mov       eax, dword [dNumA] ; 42000 * -293 / -3157   = 3898 = 0x3fa
      imul      dword [dNumC]
      idiv      dword [dNumB]
      mov       dword [dAns3], eax
      
      mov       r8,0
      mov       r8d, dword [dAns3]
      mov       r10, 8
      call      print_hex  
      
      ; qNumA       dq      730000
      ; qNumB       dq      -13456
      ; qNumC       dq      -1279
      
      mov       rax, qword [qNumA] ; 730000 / 9  = 81111 = 0x13CD7
      cqo
      mov       rbx, 9
      idiv      rbx
      mov       qword [qAns1], rax
      
      mov       r8, qword [qAns1]
      mov       r10, 16
      call      print_hex       

      mov       rax, qword [qNumA] ; 730000 / -13456  = -54 rem 0xd30
      cqo
      idiv      qword [qNumB]
      mov       qword [qAns2], rax
      mov       qword [qRem2], rdx
     
      mov       r8, qword [qAns2]
      mov       r10, 16
      call      print_hex       
      
      mov       r8, qword [qRem2]
      mov       r10, 16
      call      print_hex       

      mov       rax, qword [qNumA] ; 730000 * -1279 / -13456  = 69386 = 0x10F0A
      imul      qword [qNumC]
      idiv      qword [qNumB]
      mov       qword [qAns3], rax
      
      mov       r8, qword [qAns3]
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
 
