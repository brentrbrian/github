%include "syscalls.inc"

section   .data

bNumA     db     63
bNumB     db     17
bNumC     db      5
bAns1     db      0
bAns2     db      0
bRem2     db      0
bAns3     db      0

wNumA     dw   4321
wNumB     dw   1234
wNumC     dw    167
wAns1     dw      0
wAns2     dw      0
wRem2     dw      0
wAns3     dw      0 

dNumA     dd  42000
dNumB     dd  -3157
dNumC     dd   -293
dAns1     dd      0
dAns2     dd      0
dRem2     dd      0
dAns3     dd      0

qNumA     dq 730000
qNumB     dq -13456
qNumC     dq  -1279
qAns1     dq      0
qAns2     dq      0
qRem2     dq      0
qAns3     dq      0 
 
section .text

global main

main:
 
; bAns1 = bNumA / 3 (unsigned)
  mov  al, byte [bNumA]
  mov  ah, 0
  mov  bl, 3
  div  bl
  mov  byte [bAns1], al

; bAns2 = bNumA / bNumB (unsigned)
  mov  ax, 0
  mov  al, byte [bNumA]
  div  byte [bNumB]
  mov  byte [bAns2], al
  mov  byte [bRem2], ah

; bAns3 = (bNumA * bNumC) / bNumB (unsigned)
  mov  al, byte [bNumA]
  mul  byte [bNumC]
  div  byte [bNumB] 
  mov  byte [bAns3], al

; wAns1 = wNumA / 5 (unsigned)
  mov  ax, word [wNumA]
  mov  dx, 0
  mov  bx, 5
  div  bx
  mov  word [wAns1], ax

; wAns2 = wNumA / wNumB (unsigned)
  mov  dx, 0
  mov  ax, word [wNumA]
  div  word [wNumB]
  mov  word [wAns2], ax
  mov  word [wRem2], dx

; wAns3 = (wNumA * wNumC) / wNumB (unsigned)
  mov  ax, word [wNumA]
  mul  word [wNumC]
  div  word [wNumB]
  mov  word [wAns3], ax

; dAns1 = dNumA / 7 (signed)
  mov  eax, dword [dNumA]
  cdq 
  mov  ebx, 7
  idiv ebx
  mov  dword [dAns1], eax

; dAns2 = dNumA / dNumB (signed)
  mov  eax, dword [dNumA]
  cdq
  idiv dword [dNumB]
  mov  dword [dAns2], eax
  mov  dword [dRem2], edx

; dAns3 = (dNumA * dNumC) / dNumB (signed)
  mov  eax, dword [dNumA]
  imul dword [dNumC]
  idiv dword [dNumB]
  mov  dword [dAns3], eax

; qAns1 = qNumA / 9 (signed)
  mov  rax, qword [qNumA]
  cqo
  mov  rbx, 9
  idiv rbx
  mov  qword [qAns1], rax
  
; qAns2 = qNumA / qNumB (signed)
  mov  rax, qword [qNumA]
  cqo
  idiv qword [qNumB]
  mov  qword [qAns2], rax
  mov  qword [qRem2], rdx

; qAns3 = (qNumA * qNumC) / qNumB (signed)
  mov  rax, qword [qNumA]
  imul qword [qNumC]
  idiv qword [qNumB]
  mov  qword [qAns3], rax
  
exit:
  
  mov  rax, SYS_exit
  mov  rdi, EXIT_SUCCESS
  syscall
  

