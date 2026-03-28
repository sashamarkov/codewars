function bestServer(servers) {
  const valid = servers
    .map((s, i) => {
      const validData = s.testdata.filter(v => v !== -1);
      return {
        ...s,
        index: i,
        rate: s.testdata.filter(v => v === -1).length / 24,
        avg: validData.reduce((a,b) => a + b, 0) / validData.length
      };
    })
    .filter(s => s.price <= 500 && !s.testdata.some(v => v > 300) && s.rate <= 0.2);
  
  if (!valid.length) {
    return "";
  }
  valid.sort((a, b) => 
    a.rate - b.rate || 
    a.avg - b.avg || 
    a.price - b.price || 
    a.index - b.index
  );
  return valid[0].name;
}