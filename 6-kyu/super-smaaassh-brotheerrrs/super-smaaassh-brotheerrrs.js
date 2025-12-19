class scoreHandler {
  constructor() {
    this.scores = {};
    this.alive = {};
    this.lastHit = {};
    this.landed = {};
  }
​
  startRound(players) {
    players.forEach(player => {
      this.scores[player] = 0;
      this.alive[player] = true;
      this.lastHit[player] = null;
      this.landed[player] = false;
    });
  }
​
  handleEvent(event) {
    const [actor, actionOrTarget] = event;
​
    if (actionOrTarget === 'spawns') {
      this.handleSpawn(actor);
    } else if (actionOrTarget === 'dies') {
      this.handleDeath(actor);
    } else if (actionOrTarget === 'lands') {
      this.handleLand(actor);
    } else {
      this.handleHit(actor, actionOrTarget);
    }
  }
​
  handleSpawn(player) {
    this.alive[player] = true;
  }
​
  handleDeath(player) {
    this.alive[player] = false;
    const hitter = this.lastHit[player];
    if (hitter && !this.landed[player]) {