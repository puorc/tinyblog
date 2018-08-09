import React from "react";
import { List, Header } from "semantic-ui-react";

class Categories extends React.Component {
  render() {
    const content = this.props.data.map(item => (
      <List.Item as="a" key={item.node.id}>
        {item.node.name}
      </List.Item>
    ));
    return (
      <div>
        <Header as="h3">Categories</Header>
        <List link>{content}</List>
      </div>
    );
  }
}

export default Categories;
