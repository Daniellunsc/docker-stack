import React, { Component } from 'react';
import './App.css';
import LoginScreen from './Screens/LoginScreen';
import TodoScreen from './Screens/TodoScreen';
import ProtectedRoute from './Components/ProtectedRoute';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

class App extends Component {
  state = {
    usuario: "",
    senha: "",
  }

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <Router>
            <Switch>
              <Route exact path="/login" component={LoginScreen} />
              <Route exact path="/mytodos" component={ProtectedRoute(TodoScreen)} />
            </Switch>
          </Router>
        </div>

      </div>
    );
  }
}

export default App;
