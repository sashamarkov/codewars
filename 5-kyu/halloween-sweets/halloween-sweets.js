function pick(bags, scale) {
  let candidates = [bags.slice(0, 3), bags.slice(3, 6), bags.slice(6, 9)];
  const i = r => r === -1 ? 0 : r === 1 ? 1 : 2;
  candidates = candidates[i(scale.weigh(candidates[0], candidates[1]))];
  return candidates[i(scale.weigh([candidates[0]], [candidates[1]]))];
}