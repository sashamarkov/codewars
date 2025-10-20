class SimTime {
  constructor() {
    this.simTime = 0;
    this.lastRealTime = 0;
    this.speed = 1;
  }
  
  get() {
    return this.simTime;
  }
  
  set_speed(newSpeed) {
    this.speed = newSpeed;
  }
  
  update(currentRealtime) {
    if (currentRealtime < this.lastRealTime) {
      throw new Error;
    }
    const deltaReal = currentRealtime - this.lastRealTime;
    const deltaSim = deltaReal * this.speed;
    this.simTime += deltaSim;
    this.lastRealTime = currentRealtime;
  }
}