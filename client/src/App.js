import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  state = {
    name: "",
  }
  componentDidMount(){
    fetch('/api/message').then(res => res.json()).then(dt => this.setState({name: dt.msg}))
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            {this.state.name}
          </p>
        </header>
      </div>
    );
  }
}

export default App;
