function totalTime(arr) {
  const totalSeconds = calculateTotalSeconds(arr);
  if (totalSeconds === 0) return "0";
  const timeComponents = breakDownTime(totalSeconds);
  return formatTimeComponents(timeComponents);
}
​
function calculateTotalSeconds(arr) {
  return arr.reduce((total, timeStr) => {
    return total + parseTimeString(timeStr);
  }, 0);
}
​
function parseTimeString(timeStr) {
  const parts = timeStr.split(':').map(Number);
  const [hours, minutes, seconds] = getTimeComponents(parts);
  return hours * 3600 + minutes * 60 + seconds;
}
​
function getTimeComponents(parts) {
  switch (parts.length) {
    case 1: return [0, 0, parts[0]];
    case 2: return [0, parts[0], parts[1]];
    case 3: return [parts[0], parts[1], parts[2]];
    default: return [0, 0, 0];
  }
}
​
function breakDownTime(totalSeconds) {
  const days = Math.floor(totalSeconds / 86400);
  totalSeconds %= 86400;
  const hours = Math.floor(totalSeconds / 3600);
  totalSeconds %= 3600;
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = totalSeconds % 60;
  return { days, hours, minutes, seconds };
}
​
function formatTimeComponents(time) {
  const components = [];
  if (time.days > 0) {
    components.push(`${time.days} day${time.days > 1 ? 's' : ''}`);
  }
  if (time.hours > 0) {
    components.push(`${time.hours} hour${time.hours > 1 ? 's' : ''}`);
  }
  if (time.minutes > 0) {
    components.push(`${time.minutes} minute${time.minutes > 1 ? 's' : ''}`);
  }
  if (time.seconds > 0) {
    components.push(`${time.seconds} second${time.seconds > 1 ? 's' : ''}`);
  }
  return components.join(', ');
}