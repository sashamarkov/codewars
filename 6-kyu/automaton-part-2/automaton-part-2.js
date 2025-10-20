function automaton(e) {
  if (typeof e === 'string') {
    return (e.match(/[aeiou]/gi) || []).length;
  }
  if (typeof e === 'number') {
    if (!Number.isInteger(e) || e < 2) 
      return false;
    for (let i = 2; i <= Math.sqrt(e); i++) {
      if (e % i === 0) 
        return false;
    }
    return true;
  }
  if (typeof e === 'object') {
    const swapped = {};
    for (const key in e) {
      swapped[e[key]] = key;
    }
    return swapped;
  }
}