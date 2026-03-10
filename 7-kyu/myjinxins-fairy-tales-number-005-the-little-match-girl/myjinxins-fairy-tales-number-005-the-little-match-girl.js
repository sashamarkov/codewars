function poorGirl(matches, action) {
  let arr = matches.split('');
  for (let act of action) {
    const [type, countStr] = act.split(':');
    let count = parseInt(countStr);
    for (let i = 0; i < arr.length && count > 0; i++) {
      if (arr[i] === 'i' || arr[i] === '!') {
        if (type === 'Sell') {
          arr[i] = '$';
        } else if (type === 'Burn') {
          arr[i] = '1';
        }
        count--;
      }
    }
  }
  return arr.join('');
}