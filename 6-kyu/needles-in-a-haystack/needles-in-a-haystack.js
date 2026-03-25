function search(haystack, needle) {
  const results = [];
  const stack = [{ obj: haystack, path: '' }];
  
  while (stack.length) {
    const { obj, path } = stack.pop();
    for (const key in obj) {
      const value = obj[key];
      const currentPath = path ? `${path}.${key}` : key;
      if (typeof value === 'string' && value.includes(needle)) {
        results.push(currentPath);
      }
      if (value && typeof value === 'object') {
        stack.push({ obj: value, path: currentPath });
      }
    }
  }
  return results.sort();
}