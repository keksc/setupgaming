bits 64
default rel

%define endl 0xd, 0xa

segment .data
    welcomeMsg db "Welcome to Isola", endl, "top = z", endl, "right = d", endl, "down = s", endl, "left = q", endl, 0
    enterPosMsg db "", 0
    board dd 1, 2, 3, 4
    showInt db "%i", 0

segment .bss
    
    

segment .text
global main
extern ExitProcess

extern printf, scanf

main:
    push    rbp
    mov     rbp, rsp
    sub     rsp, 32

    lea rcx, [welcomeMsg]
    call printf

    lea rcx, [showInt]
    mov rdx, [board + 3]
    call printf

    xor     rax, rax
    call    ExitProcess
