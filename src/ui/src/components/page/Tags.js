import React from "react";
import { Label, Header } from "semantic-ui-react";

class Tags extends React.Component {
  render() {
    const content = this.props.data.map(item => (
      <Label as="a" key={item.node.id}>
        {item.node.name}
      </Label>
    ));
    return (
      <div style={{ marginTop: "20px" }}>
        <Header as="h3">Tags</Header>
        {content}
      </div>
    );
  }
}

export default Tags;
