function automaton(e) {
  const strategies = {
    string: (s) => {
      const vowels = {a:0,e:0,i:0,o:0,u:0};
      for (let char of s.toLowerCase()) {
        if (vowels.hasOwnProperty(char)) vowels[char]++;
      }
      Object.keys(vowels).forEach(v => { 
        if (vowels[v] === 0) delete vowels[v]; 
      });
      return vowels;
    },
    number: (n) => {
      const primes = [];
      const max = Math.floor(n);
      for (let i = 2; i <= max; i++) {
        let isPrime = true;
        for (let j = 2; j <= Math.sqrt(i); j++) {
          if (i % j === 0) {
            isPrime = false;
            break;
          }
        }
        if (isPrime) primes.push(i);
      }
      return primes;
    },
    object: (obj) => {
      const keys = Object.keys(obj).sort();
      const values = keys.map(k => String(obj[k]));
      return [keys.length, keys, values];
    }
  };
  return strategies[typeof e](e);
}