section .text
global mod
mod:
    push rbx
    
    mov rax, rdi
    
    xor rdx, rdx
    div rsi
    mov rax, rdx
    pop rbx
    
    ret