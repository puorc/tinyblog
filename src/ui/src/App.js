import React, { Component } from "react";
import { Route, Switch } from "react-router-dom";
import Page from "./components/page/Home";
import Layout from "./components/dashboard/Home";
import Login from "./components/Login";
import "./App.css";

class App extends Component {
  render() {
    return (
      <Switch>
        <Route exact path="/" component={Page} />
        <Route path="/login" component={Login} />
        <Route path="/dashboard" component={Layout} />
      </Switch>
    );
  }
}

export default App;
