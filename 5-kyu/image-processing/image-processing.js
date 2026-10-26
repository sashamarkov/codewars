const clamp = (v, max) => v < 0 ? 0 : v > max ? max : v;
​
function processImage(imageData, height, width, weights) {
  const result = [];
  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      result.push(...processPixel(imageData, height, width, weights, y, x));
    }
  }
  return result;
}
​
function processPixel(imageData, height, width, weights, y, x) {
  const n = weights.length;
  const r = Math.floor(n / 2);
  const rgb = [0, 0, 0];
  for (let dy = -r; dy <= r; dy++) {
    const yy = clamp(y + dy, height - 1);
    for (let dx = -r; dx <= r; dx++) {
      const xx = clamp(x + dx, width - 1);
      const w = weights[dy + r][dx + r];
      const pixelNumber =  (yy * width + xx);
      const j = pixelNumber * 3;
      for (let i = 0; i < 3; i++) {
        rgb[i] += imageData[j + i] * w;
      }
    }
  }
  return rgb.map(v => clamp(Math.round(v), 255));
}