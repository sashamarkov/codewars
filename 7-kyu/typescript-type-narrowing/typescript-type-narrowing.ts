export function isPair<T>(arr: T[]): arr is [T, T] {
  return arr.length === 2;
}