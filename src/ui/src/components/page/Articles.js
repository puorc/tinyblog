import React from "react";
import { List, Icon, Pagination } from "semantic-ui-react";

class Articles extends React.Component {
  render() {
    const content = this.props.data.slice(0, 10).map(item => (
      <List.Item key={item.node.id}>
        <List.Icon
          name="calendar alternate outline"
          size="large"
          verticalAlign="middle"
        />
        <List.Content>
          <List.Header as="a">{item.node.title}</List.Header>
          <List.Description as="a">
            <span>
              <Icon name="database" />
              {item.node.category.name}
            </span>
            <span style={{ marginLeft: "10px" }}>
              <Icon name="user" />
              {item.node.author.username}
            </span>
          </List.Description>
        </List.Content>
      </List.Item>
    ));
    return (
      <List divided relaxed>
        {content}
        <div style={{ marginTop: "15px", float: "right" }}>
          <Pagination defaultActivePage={1} totalPages={10} />
        </div>
      </List>
    );
  }
}

export default Articles;
