app.filter("fileSize", function() {
  return function(bytes) {
    if (!bytes || bytes < 0) {
      return '0 B';
    }
    const units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB'];
    let size = bytes;
    let i = 0;
    while (size >= 1024 && i < units.length - 1) {
      size /= 1024;
      i++;
    }
    const formatted = i === 0 ? Math.round(size) : size.toFixed(2);
    return formatted + ' ' + units[i];
  };
});
​