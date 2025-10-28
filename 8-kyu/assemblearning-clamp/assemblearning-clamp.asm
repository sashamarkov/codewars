section .text
global clamp
​
clamp:
    ; Inputs: rdi = a, rsi = lo, rdx = hi
    ; Output: rax = clamped value
​
    cmp rdi, rsi
    jb .below_lo 
​
    cmp rdi, rdx
    ja .above_hi 
​
    mov rax, rdi
    ret
​
.below_lo:
    mov rax, rsi
    ret
​
.above_hi:
    mov rax, rdx
    ret