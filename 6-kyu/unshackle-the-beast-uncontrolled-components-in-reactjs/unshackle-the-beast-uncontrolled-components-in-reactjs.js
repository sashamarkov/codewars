const React = require("react");
​
class BeastForm extends React.Component {
  constructor(props) {
    super(props);
    this.beastToRelease = { value: '' };
    this.handleSubmit = this.handleSubmit.bind(this);
  }
​
  handleSubmit(e) {
    e.preventDefault();
    unshackle(this.beastToRelease.value);
  }
​
  render() {
    return (
      <form id="beastForm" onSubmit={this.handleSubmit}>
        <input id="beastToRelease" defaultValue={this.beastToRelease.value} />
        <button id="submit" type="submit">Release</button>
      </form>
    );
  }
}
​
module.exports = BeastForm;