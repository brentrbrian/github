;
; ABS value <reg>
; 
%macro  ABS     1
      cmp       %1, 0
      jge       %%done
      neg       %1
%%done:
%endmacro


;
; PRINT <pointer> 
;
%macro PRINT 2
      mov       rax, SYS_write
      mov       rdi, STDOUT
      mov       rsi, %1
      mov       rdx, %2
      syscall
%endmacro
