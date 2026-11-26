function findSpecialIdx(vms) {
  for (let i = 0; i < 100; i++) {
    for (let j = 0; j < i; j++) {
      vms[i].vend();
    }
  }
  return vms.weigh() - 4950 * 100;
};