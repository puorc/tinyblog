import React from "react";
import { List, Icon } from "semantic-ui-react";

class Articles extends React.Component {
  render() {
    const content = this.props.data.map(item => (
      <List.Item key={item.node.id}>
        <List.Icon
          name="calendar alternate outline"
          size="large"
          verticalAlign="middle"
        />
        <List.Content>
          <List.Header as="a">{item.node.title}</List.Header>
          <List.Description as="a">
            <Icon name="database" />
            {item.node.category.name}
            <Icon name="tags" />> tags
            <Icon name="user" />
            {item.node.author.username}
          </List.Description>
        </List.Content>
      </List.Item>
    ));
    return (
      <List divided relaxed>
        {content}
      </List>
    );
  }
}

export default Articles;
