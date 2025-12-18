function validateRace(moves) {
    const starts = moves.map((m, i) => i + 1 + m);
    const set = new Set(starts);
    return starts.every(s => s >= 1 && s <= moves.length) && set.size === moves.length;
}