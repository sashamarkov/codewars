class HallOfFame {
    constructor(size = 5, players = []) {
        this.size = size;
        this.players = [];
        players.forEach(p => this.add(p));
    }
​
    get list() {
        return Array.from({length: this.size}, (_, i) => 
            i < this.players.length ? `${this.players[i][0]}: ${this.players[i][1]}` : ""
        );
    }
​
    add(player) {
        this.players.push([player[0], +player[1]]);
        this.players.sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
        this.players = this.players.slice(0, this.size);
        return this;
    }
}