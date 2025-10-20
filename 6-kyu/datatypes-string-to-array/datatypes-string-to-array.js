function dataTypes(str) {
    const tokens = str.match(/\d+|true|false|[^\s\d]+?(?=\d|\s|true|false|$)/gi) || [];
    return tokens.map(token => {
        if (/^\d+$/.test(token)) return 'number';
        if (/^true|false$/i.test(token)) return 'boolean';
        return 'string';
    });
}