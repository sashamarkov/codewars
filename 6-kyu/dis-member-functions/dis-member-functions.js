function dismember (func) {
    const str = func.toString();
    const params = str.substring(str.indexOf('(') + 1, str.indexOf(')')).trim();
    if (!params) {
        return [];
    }
    return params.split(',').map(p => p.trim());
}