%include "syscalls.inc"

section   .data

bMask     db 0x0f
bAscii    db 0x30
bNum      db 0

dNum      dd 0x12345678

result    dw '0x'
hexq      dq 0
          db LF
resLen    equ $-result
 
section .text

global main

main:

        mov     r8d, dword [dNum]
        mov     r10,8

shift_loop:

        shl     r9,8

        mov     r9b, r8b
        and     r9b, byte [bMask]
        or      r9b, byte [bAscii]


        ror     r8d,4
        
        dec     r10
        cmp     r10, 0
        jne     shift_loop 
        
        mov     qword [hexq], r9
  
                                        ; write(1, msg, msglen)
        mov     rax,1                   ; system call 1 is write
        mov     rdi,1                   ; file handle 1 is stdout
        mov     rsi,result              ; address of string to output
        mov     rdx,resLen              ; number of bytes
        syscall                         ; invoke operating system to do the write
        

                                        ; exit(0)
        mov     rax,60                  ; system call 60 is exit
        xor     rdi,rdi                 ; we want return code 0
        syscall                         ; invoke operating system to exit
  
  
exit:
  
        mov  rax, SYS_exit
        mov  rdi, EXIT_SUCCESS
        syscall
        
msg:    db      '0x'
msglen: equ     $-msg  
  

