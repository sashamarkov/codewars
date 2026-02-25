export const toggleBit = (n: number, position: number): number => {
  return n ^ (1 << position);
};
​
export const setBit = (n: number, position: number): number => {
  return n | (1 << position);
};
​
export const clearBit = (n: number, position: number): number => {
  return n & ~(1 << position);
};
​
export const isBitSet = (n: number, position: number): boolean => {
  return (n & (1 << position)) !== 0;
};
​
export const setMultipleBits = (n: number, mask: number): number => {
  return n | mask;
};
​
export const clearMultipleBits = (n: number, mask: number): number => {
  return n & ~mask;
};
​
export const toggleMultipleBits = (n: number, mask: number): number => {
  return n ^ mask;
};
​