function switchLift(status, n) {
    const { distances, hasLiftAtFloor } = calculateDistances(status, n);
    
    if (hasLiftAtFloor) return "";
    
    return findClosestLifts(distances).join('');
}
​
function canLiftReach(lift, floor) {
    if (lift === 'A') {
        return floor % 2 === 1;
    } else if (lift === 'B') {
        return floor === 1 || floor % 2 === 0;
    } else {
        return true;
    }
}
​
function calculateDistances(status, n) {
    const lifts = ['A', 'B', 'C'];
    const distances = {};
    let hasLiftAtFloor = false;
    
    lifts.forEach(lift => {
        const currentFloor = status[lift];
        
        if (currentFloor === n) {
            hasLiftAtFloor = true;
        }
        
        if (canLiftReach(lift, n)) {
            const distance = Math.abs(currentFloor - n);
            if (distance > 0) {
                distances[lift] = distance;
            }
        }
    });
    
    return { distances, hasLiftAtFloor };
}
​
function findClosestLifts(distances) {
    const lifts = ['A', 'B', 'C'];
    const distanceValues = Object.values(distances);
    if (distanceValues.length === 0) return [];
    
    const minDistance = Math.min(...distanceValues);
    
    return lifts.filter(lift => distances[lift] === minDistance).sort();
}
​