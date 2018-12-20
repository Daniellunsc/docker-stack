import React, { Component } from 'react';
import '../App.css';
import {Redirect} from 'react-router-dom';

class App extends Component {
  state = {
    usuario: "",
    senha: "",
    fireRedirect: false,
    redirectTo: ""
  }

  submit = (e) => {
    const { location } = this.props;
    let path = location.state ? location.state.from.pathname : "/"
    e.preventDefault()
    fetch('/auth', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username: this.state.usuario, password: this.state.senha })
    })
      .then(res => res.json())
      .then(dt => {
        if (dt.status === "success") {
          this.setState({
            fireRedirect: true,
            redirectTo: path
          });
        }
      })
  }

  onChange = e => {
    const { value, name } = e.target
    this.setState({ [name]: value })
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <form>
            <input name='usuario' type="text" placeholder="Usuário" value={this.state.usuario} onChange={this.onChange} />
            <input name='senha' type="password" placeholder="Senha" value={this.state.senha} onChange={this.onChange} />
            <button onClick={this.submit}>Logar</button>
          </form>
          <p>
            {this.state.name}
          </p>
        </header>
        {this.state.fireRedirect && <Redirect to={this.state.redirectTo} />}
      </div>
    );
  }
}

export default App;
