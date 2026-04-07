global absolute_value
absolute_value: mov rax, rdi
  neg rax
  cmovs rax, rdi
  ret