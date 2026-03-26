function dateFilter(date, format) {
  const dateObj = parseDate(date);
  const formatters = createFormatters(dateObj);
  return formatDate(format, formatters);
}
​
function parseDate(date) {
  if (typeof date === 'string' && !isNaN(Number(date))) {
    return new Date(Number(date));
  }
  return new Date(date);
}
​
function createFormatters(date) {
  return {
    year: () => date.getFullYear(),
    yearShort: () => date.getFullYear() % 100,
    month: () => date.getMonth() + 1,
    day: () => date.getDate(),
    hour: () => date.getHours(),
    minute: () => date.getMinutes(),
    second: () => date.getSeconds()
  };
}
​
function pad(num, length) {
  return String(num).padStart(length, '0');
}
​
function formatDate(format, formatters) {
  const patterns = [
    { pattern: 'yyyy', value: () => pad(formatters.year(), 4) },
    { pattern: 'yy', value: () => pad(formatters.yearShort(), 2) },
    { pattern: 'MM', value: () => pad(formatters.month(), 2) },
    { pattern: 'M', value: () => formatters.month() },
    { pattern: 'dd', value: () => pad(formatters.day(), 2) },
    { pattern: 'd', value: () => formatters.day() },
    { pattern: 'HH', value: () => pad(formatters.hour(), 2) },
    { pattern: 'H', value: () => formatters.hour() },
    { pattern: 'mm', value: () => pad(formatters.minute(), 2) },
    { pattern: 'm', value: () => formatters.minute() },
    { pattern: 'ss', value: () => pad(formatters.second(), 2) },
    { pattern: 's', value: () => formatters.second() }
  ];
  
  let result = format;
  for (let { pattern, value } of patterns) {
    result = result.replace(new RegExp(pattern, 'g'), value());
  }
  
  return result;
}