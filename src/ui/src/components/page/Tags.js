import React from "react";
import { Label, Icon, Header } from "semantic-ui-react";

class Tags extends React.Component {
  render() {
    const content = this.props.data.map(item => (
      <Label as="a" key={item.node.id}>
        {item.node.name}
      </Label>
    ));
    return (
      <div>
        <Header as="h3">Tags</Header>
        {content}
      </div>
    );
  }
}

export default Tags;
