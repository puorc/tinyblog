import React from "react";
import { Header } from "semantic-ui-react";

class Head extends React.Component {
  render() {
    return (
      <div style={{ marginTop: "10px", marginBottom: "15px" }}>
        <Header className="title" as="h2">Tiny Blog</Header>
        <Header className="description" as="h5">just another blog</Header>
      </div>
    );
  }
}

export default Head;
