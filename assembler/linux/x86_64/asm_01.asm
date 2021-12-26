;
; print argv[0]
;

%include "syscalls.inc"

section       .data

newLine       db   LF,NULL

section       .text

global        main
global        PRINT_STRING

main:

  mov   r12,rdi
  mov   r13,rsi 

printArguments:

  mov   rdi,newLine
  call  PRINT_STRING
  
  mov   rbx,0

printLoop:

  mov   rdi,qword [r13+rbx*8]
  call  PRINT_STRING
  mov   rdi,newLine
  call  PRINT_STRING
  inc   rbx
  cmp   rbx,r12
  jl    printLoop

exit:

  mov   rax,SYS_exit
  mov   rdi,EXIT_SUCCESS
  syscall
  
;
; FUNCTIONS
;

PRINT_STRING:

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


