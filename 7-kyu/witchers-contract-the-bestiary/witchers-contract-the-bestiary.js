function identifyMonster(observedWeaknesses, bestiary) {
  for (const [monster, weaknesses] of Object.entries(bestiary)) {
    if (observedWeaknesses.every(weakness => weaknesses.includes(weakness))) {
      return monster;
    }
  }
  return "Unknown monster";
}