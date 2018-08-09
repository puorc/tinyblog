import React from "react";
import { Button, Header, Dropdown, Input } from "semantic-ui-react";
import ArticleList from "./ArticleList";

const tagOptions = [
  {
    text: "Important",
    value: "Important",
    label: { color: "red", empty: true, circular: true }
  }
];

const TableExampleFullWidth = () => (
  <div>
    <Header as="h2">
      <Header.Content>Posts</Header.Content>
    </Header>
    <Button content="Add Post" icon="plus" labelPosition="left" />
    <Button content="Delete" icon="trash" labelPosition="left" />
    <Dropdown
      text="Filter Posts"
      icon="filter"
      floating
      labeled
      button
      className="icon">
      <Dropdown.Menu>
        <Input icon="search" iconPosition="left" className="search" />
        <Dropdown.Divider />
        <Dropdown.Header icon="tags" content="Tag Label" />
        <Dropdown.Menu scrolling>
          {tagOptions.map(option => (
            <Dropdown.Item key={option.value} {...option} />
          ))}
        </Dropdown.Menu>
      </Dropdown.Menu>
    </Dropdown>
    <ArticleList />
  </div>
);

export default TableExampleFullWidth;
