function factory(assemblyLines) {
  const items = [];
  for (let i = 0; i < assemblyLines.length; i++) {
    const line = assemblyLines[i];
    items.push(...(typeof line === 'function' ? line() : line));
  }
  items.sort((a, b) => a.priority - b.priority);
  
  const itemNames = items.map(item => item.item);
  const shipments = [];
  for (let i = 0; i < itemNames.length; i += 10) {
    shipments.push(itemNames.slice(i, i + 10));
  }
  return shipments;
}