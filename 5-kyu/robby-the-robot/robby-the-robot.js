  turnRight(dir) {
    return (dir + 1) % 4;
  }
  
  turnLeft(dir) {
    return (dir + 3) % 4;
  }
  
  findPath(maxPower) {
    const queue = [{
      x: this.start.x,
      y: this.start.y,
      dir: 0,
      commands: [],
      cost: 0
    }];
    
    const visited = new Set();
    
    while (queue.length) {
      const current = queue.shift();
      const {x, y, dir, commands, cost} = current;
      
      const key = `${x},${y},${dir}`;
      if (visited.has(key)) continue;
      visited.add(key);
      
      if (x === this.target.x && y === this.target.y) return commands;
      if (cost >= maxPower) continue;
      
      this.tryMoveForward(current, queue, commands, cost);
      this.tryTurn(current, queue, commands, cost, 'r');
      this.tryTurn(current, queue, commands, cost, 'l');
    }
    
    return [];
  }
  
  tryMoveForward(current, queue, commands, cost) {
    const {x, y, dir} = current;
    const next = this.moveForward(x, y, dir);
    if (this.isWalkable(next.x, next.y)) {
      queue.push({
        x: next.x, y: next.y, dir,
        commands: [...commands, 'f'],
        cost: cost + 1
      });
    }
  }
  
  tryTurn(current, queue, commands, cost, turnDir) {
    const newDir = turnDir === 'r' ? this.turnRight(current.dir) : this.turnLeft(current.dir);
    queue.push({
      x: current.x, y: current.y, dir: newDir,
      commands: [...commands, turnDir],
      cost: cost + 1
    });
  }
}
​
function getCommands(field, power) {
  const pathfinder = new RobbyPathfinder(field);
  return pathfinder.findPath(power);
}