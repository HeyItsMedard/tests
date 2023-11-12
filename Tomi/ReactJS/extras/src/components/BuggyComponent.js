import { Component } from 'react'

class BuggyCounter extends Component {
  constructor(props) {
    super(props)
    this.state = { counter: 0 }
    this.handleClick = this.handleClick.bind(this)
  }
  handleClick = () => this.setState({ counter: this.state.counter + 1 })
  render() {
    if (this.state.counter === 5) {
      throw new Error('not allowed value')
    }
    return (
      <div>
        <button onClick={this.handleClick}>increase</button>
        value:{this.state.counter}
      </div>
    )
  }
}

export default BuggyCounter
