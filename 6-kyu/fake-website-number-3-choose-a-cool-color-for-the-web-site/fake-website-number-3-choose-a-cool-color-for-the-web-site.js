function rgb2Hsl(color){
  let rgb = parseHex(color);
  if(!rgb) {
    return "color: hsl(0,0%,100%)";
  }
  let hsl = rgbToHsl(rgb.r, rgb.g, rgb.b);
  return `color: hsl(${hsl.h},${hsl.s}%,${hsl.l}%)`;
}
​
function parseHex(color) {
  let match = color.match(/^color: #([0-9a-f]{6})$/i);
  if(!match) {
    return null;
  }
  return {
    r: parseInt(match[1].slice(0,2),16) / 255,
    g: parseInt(match[1].slice(2,4),16) / 255,
    b: parseInt(match[1].slice(4,6),16) / 255
  };
}
​
function rgbToHsl(r,g,b) {
  let max = Math.max(r,g,b);
  let min = Math.min(r,g,b);
  let h, s, l = (max + min) / 2;
  if(max === min){
    h = s = 0;
  } else {
    let d = max - min;
    s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
    switch(max){
      case r: h = (g - b) / d + (g < b ? 6 : 0); break;
      case g: h = (b - r) / d + 2; break;
      case b: h = (r - g) / d + 4; break;
    }
    h = (h / 6);     
  }
  return { h: Math.round(h * 360), s: Math.round(s * 100), l: Math.round(l * 100) };
}