function getTagContent(htmlString, tag) {
  const pattern = new RegExp(`<${tag}[^>]*>([\\s\\S]*?)</${tag}>`, 'g');
  const result = [];
  let match;
  while ((match = pattern.exec(htmlString)) !== null) {
    result.push(match[1].trim());
  }
  return result;
}