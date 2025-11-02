function getGrowth(...args) {
    return args.map((current, i) => {
        if (i === 0) return `${current} (+0, +0%)`;
        const prev = args[i - 1];
        const diff = current - prev;
        const percent = Math.round((diff / prev) * 100);
        return `${current} (${diff >= 0 ? '+' : ''}${diff}, ${percent >= 0 ? '+' : ''}${percent}%)`;
    }).join(', ');
}