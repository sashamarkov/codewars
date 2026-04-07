global are_same_case
are_same_case: xor dil, sil
  test dil, 0x20
  sete al
  ret