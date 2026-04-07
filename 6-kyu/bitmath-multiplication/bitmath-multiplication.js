class BitMath {
  static multiply(a, b) {
    let result = 0;
    while (b !== 0) {
      if (b & 1) result = BitMath.add(result, a);
      a <<= 1;
      b >>>= 1;
    }
    return result;
  }
  
  static add(a, b) {
    while (b !== 0) {
      let carry = a & b;
      a = a ^ b;
      b = carry << 1;
    }
    return a;
  }
}