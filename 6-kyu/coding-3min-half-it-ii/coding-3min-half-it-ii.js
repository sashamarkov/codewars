function halfIt(n) {
  if (typeof n !== 'number' || !Number.isInteger(n)) {
    return 0;
  }
  const binary = Math.abs(n).toString(2);
  const halfBinary = binary.replace(/([01])\1*/g, match => 
    match.slice(0, Math.ceil(match.length / 2))
  );
  return Math.sign(n) * parseInt(halfBinary, 2);
}