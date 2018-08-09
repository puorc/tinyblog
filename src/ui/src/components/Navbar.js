import React from "react";
import { Container, Dropdown, Menu, Icon } from "semantic-ui-react";

const Navbar = () => (
  <Menu fixed="top" inverted>
    <Container>
      <Menu.Item as="a" header>
        <Icon name="coffee" size="big" />
        Tiny Blog
      </Menu.Item>
      <Menu.Item as="a">Dashboard</Menu.Item>
      <Dropdown item simple text="Posts">
        <Dropdown.Menu>
          <Dropdown.Item>All Posts</Dropdown.Item>
          <Dropdown.Item>Add New</Dropdown.Item>
          <Dropdown.Item>Categories</Dropdown.Item>
          <Dropdown.Item>Tags</Dropdown.Item>
        </Dropdown.Menu>
      </Dropdown>
      <Menu.Item as="a">Comments</Menu.Item>
      <Menu.Item as="a">Themes</Menu.Item>
      <Dropdown item simple text="Users">
        <Dropdown.Menu>
          <Dropdown.Item>All Users</Dropdown.Item>
          <Dropdown.Item>Add New</Dropdown.Item>
          <Dropdown.Item>Your Profile</Dropdown.Item>
        </Dropdown.Menu>
      </Dropdown>
      <Dropdown item simple text="Settings">
        <Dropdown.Menu>
          <Dropdown.Item>General</Dropdown.Item>
          <Dropdown.Item>Reading</Dropdown.Item>
          <Dropdown.Item>Discussion</Dropdown.Item>
          <Dropdown.Item>Permalinks</Dropdown.Item>
        </Dropdown.Menu>
      </Dropdown>
      <Menu.Menu as="a" position="right">
        <Menu.Item as="a" header>
          <Icon name="log out" />
          Log Out
        </Menu.Item>
      </Menu.Menu>
    </Container>
  </Menu>
);

export default Navbar;
