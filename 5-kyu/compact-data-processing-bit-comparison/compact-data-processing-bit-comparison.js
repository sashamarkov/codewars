function Network(count) {
  this.cameras = [];
  for (var i = 0; i < count; i++)
    this.cameras.push(new Camera(0, -30));
}
​
Network.prototype.process = function(byte) {
  var id = byte & 15;
  if (id < this.cameras.length) {
    var up = (byte & 16) ? 5 : 0;
    var down = (byte & 32) ? -5 : 0;
    var left = (byte & 64) ? -5 : 0;
    var right = (byte & 128) ? 5 : 0;
    this.cameras[id].move(left + right, up + down);
  }
}
​
function Camera(h, v) {
  this.horizontal = h;
  this.vertical = v;
}
​
Camera.prototype.move = function(h, v) {
  this.horizontal = Math.min(45, Math.max(-45, this.horizontal + h));
  this.vertical = Math.min(45, Math.max(-45, this.vertical + v));
}