%include "syscalls.inc"

section .data


section .text

global  main

main:   
                                        ; write(1, msg, msglen)
        mov     rax,1                   ; system call 1 is write
        mov     rdi,1                   ; file handle 1 is stdout
        mov     rsi,msg                 ; address of string to output
        mov     rdx,msglen              ; number of bytes
        syscall                         ; invoke operating system to do the write

                                        ; exit(0)
        mov     rax,60                  ; system call 60 is exit
        xor     rdi,rdi                 ; we want return code 0
        syscall                         ; invoke operating system to exit
        
msg:    db      'hello world',LF
msglen: equ     $-msg       
        
