function transform(source, target) {
    const result = [source];
    const current = [...source];  
    for (let i = 0; i < source.length; i++) {
        if (current[i] !== target[i]) {
            current[i] = target[i];
            result.push(current.join(''));
        }
    }
    return result;
}