; ------------------------------------------------------
; Command Line Arguments Example
; 
; read command line arguments and print them
;
; ------------------------------------------------------

section       .data

LF            equ  10
NULL          equ  0
TRUE          equ  1
FALSE         equ  0

EXIT_SUCCESS  equ  0 

STDIN         equ  0
STDOUT        equ  1
STDERR        equ  2

SYS_read      equ  0
SYS_write     equ  1
SYS_open      equ  2
SYS_close     equ  3
SYS_fork      equ  57
SYS_exit      equ  60
SYS_creat     equ  85
SYS_time      equ  201

newLine       db   LF,NULL

section       .text

global        main
global        printString

main:

  mov   r12,rdi
  mov   r13,rsi 

printArguments:

  mov   rdi,newLine
  call  printString
  
  mov   rbx,0

printLoop:

  mov   rdi,qword [r13+rbx*8]
  call  printString
  mov   rdi,newLine
  call  printString
  inc   rbx
  cmp   rbx,r12
  jl    printLoop

exampleDone:

  mov   rax,SYS_exit
  mov   rdi,EXIT_SUCCESS
  syscall

printString:

  push  rbp
  mov   rbp,rsp
  push  rbx

  mov   rbx,rdi
  mov   rdx,0

strCountLoop:

  cmp   byte [rbx],NULL
  je    strCountDone
  inc   rdx
  inc   rbx
  jmp   strCountLoop

strCountDone:

  cmp   rdx,0
  je    prtDone

  mov   rax,SYS_write
  mov   rsi,rdi
  mov   edi,STDOUT
  syscall

prtDone:

  pop   rbx
  pop   rbp
  ret


