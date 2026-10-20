function rearrangeApps(tiles) {
    const a = tiles.slice();
    let i = 0;
    let j = a.length - 1;
    while (i < j) {
        if (a[i] !== null) {
          i += 1 
          continue; 
        }
        if (a[j] === null) { 
          j -= 1; 
          continue; 
        }
        [a[i], a[j]] = [a[j], a[i]];
        i += 1; 
        j -= 1;
    }
    return a.filter(x => x !== null);
}