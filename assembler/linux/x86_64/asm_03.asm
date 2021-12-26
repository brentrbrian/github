;
; asm_03.asm
;
; x86-64 Assembly Language Programming with Ubuntu 
;
; Ed Jorgensen, Ph.D.
; Version 1.1.40
; January 2020
;

      %include    "syscalls.inc"

      section     .data

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

      mov       al, byte [bNumA]
      mov       ah, 0
      mov       bl, 3
      div       bl
      mov       byte [bAns1], al

      mov       ax, 0
      mov       al, byte [bNumA]
      div       byte [bNumB]
      mov       byte [bAns2], al
      mov       byte [bRem2], ah

      mov       al, byte [bNumA]
      mul       byte [bNumC]
      div       byte [bNumB]
      mov       byte [bAns3], al

      mov       ax, word [wNumA]
      mov       dx, 0
      mov       bx, 5
      div       bx
      mov       word [wAns1], ax

      mov       dx, 0
      mov       ax, word [wNumA]
      div       word [wNumB]
      mov       word [wAns2], ax
      mov       word [wRem2], dx

      mov       ax, word [wNumA]
      mul       word [wNumC]
      div       word [wNumB]
      mov       word [wAns3], ax

      mov       eax, dword [dNumA]
      cdq
      mov       ebx, 7
      idiv      ebx
      mov       dword [dAns1], eax

      mov       eax, dword [dNumA]
      cdq
      idiv      dword [dNumB]
      mov       dword [dAns2], eax
      mov       dword [dRem2], edx

      mov       eax, dword [dNumA]
      imul      dword [dNumC]
      idiv      dword [dNumB]
      mov       dword [dAns3], eax

      mov       rax, qword [qNumA]
      cqo
      mov       rbx, 9
      idiv      rbx
      mov       qword [qAns1], rax

      mov       rax, qword [qNumA]
      cqo
      idiv      qword [qNumB]
      mov       qword [qAns2], rax
      mov       qword [qRem2], rdx

      mov       rax, qword [qNumA]
      imul      qword [qNumC]
      idiv      qword [qNumB]
      mov       qword [qAns3], rax

exit:

      mov       rax, SYS_exit
      mov       rdi, EXIT_SUCCESS
      syscall


