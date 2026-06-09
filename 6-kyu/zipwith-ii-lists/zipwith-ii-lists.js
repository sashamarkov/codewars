function zipWith(fn, head0, head1) {
  if(head0 === null || head1 === null) {
    return null;
  }
  const value = fn(head0.value, head1.value);
  const next = zipWith(fn, head0.next, head1.next);
  return new Node(value, next);
}