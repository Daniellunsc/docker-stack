import React from "react";
import { Redirect } from "react-router-dom";
import {CheckAuth} from '../Services/AuthService';

const protectedRoute = ComponentToProtect => {
  return class extends React.Component {
    state = {
      auth: false,
      loading: true
    };

    componentDidMount() {
      CheckAuth().then(res => {
        this.setState({
          auth: res.status >= 200 && res.status < 300 ? true : false,
          loading: false
        });
      });
    }

    render() {
      console.log(ComponentToProtect)
      const { auth, loading } = this.state;
      console.log(this.state);
      if (loading) {
        return <div>...</div>;
      } else if (!loading) {
        if (!auth) {
          return <Redirect to={{
            pathname: '/login',
            state: {from: this.props.location }
          }} />;
        }
        return <ComponentToProtect {...this.props} />;
      }
    }
  };
};

export default protectedRoute;