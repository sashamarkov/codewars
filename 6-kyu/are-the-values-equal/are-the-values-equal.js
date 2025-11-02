function areEqual(value1, value2) {
  if (value1 === value2) return true;
  
  if (!areObjects(value1, value2)) {
    return false;
  }
  
  if (Array.isArray(value1) && Array.isArray(value2)) {
    return areArraysEqual(value1, value2);
  }
  
  if (!Array.isArray(value1) && !Array.isArray(value2)) {
    return areObjectsEqual(value1, value2);
  }
  
  return false;
}
​
function areObjects(value1, value2) {
  return typeof value1 === 'object' && 
         typeof value2 === 'object' && 
         value1 !== null && 
         value2 !== null;
}
​
function areArraysEqual(arr1, arr2) {
  if (arr1.length !== arr2.length) return false;
  const copy1 = [...arr1];
  const copy2 = [...arr2];
  for (let i = 0; i < copy1.length; i++) {
    let foundMatch = false;
    for (let j = 0; j < copy2.length; j++) {
      if (areEqual(copy1[i], copy2[j])) {
        copy2.splice(j, 1);
        foundMatch = true;
        break;
      }
    }
    if (!foundMatch) return false;
  }
  return true;
}
​
function areObjectsEqual(obj1, obj2) {
  const keys1 = Object.keys(obj1);
  const keys2 = Object.keys(obj2);
  if (keys1.length !== keys2.length) return false;
  for (const key of keys1) {
    if (!keys2.includes(key)) return false;
    if (!areEqual(obj1[key], obj2[key])) return false;
  }
  return true;
}