import React from "react";
import { Container, Dropdown, Menu, Icon } from "semantic-ui-react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import Dashboard from "./Dashboard";
import ArticleList from "./ArticleList";

const Layout = ({ match }) => (
  <Container style={{ marginTop: "80px", marginLeft: "90px" }}>
    <Menu fixed="top" inverted>
      <Container>
        <Menu.Item as="a" header>
          <Icon name="coffee" size="big" />
          <Link to="/">Tiny Blog</Link>
        </Menu.Item>
        <Menu.Item as="a">
          <Link to="/dashboard">Dashboard</Link>
        </Menu.Item>
        <Dropdown item simple text="Posts">
          <Dropdown.Menu>
            <Dropdown.Item>
              <Link to={`${match.url}/posts`}>All Posts</Link>
            </Dropdown.Item>
            <Dropdown.Item>
              <Link to={`${match.url}/newpost`}>Add New</Link>
            </Dropdown.Item>
            <Dropdown.Item>
              <Link to={`${match.url}/categories`}>Categories</Link>
            </Dropdown.Item>
            <Dropdown.Item>
              <Link to={`${match.url}/tags`}>Tags</Link>
            </Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
        <Menu.Item as="a">
          <Link to={`${match.url}/comments`}>Comments</Link>
        </Menu.Item>
        <Menu.Item as="a">
          <Link to={`${match.url}/theme`}>Theme</Link>
        </Menu.Item>
        <Dropdown item simple text="Users">
          <Dropdown.Menu>
            <Dropdown.Item>
              <Link to={`${match.url}/users`}>All Users</Link>
            </Dropdown.Item>
            <Dropdown.Item>
              <Link to={`${match.url}/newuser`}>Add User</Link>
            </Dropdown.Item>
            <Dropdown.Item>
              <Link to={`${match.url}/profile`}>Your Profile</Link>
            </Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
        <Dropdown item simple text="Settings">
          <Dropdown.Menu>
            <Dropdown.Item>
              <Link to={`${match.url}/general`}>General</Link>
            </Dropdown.Item>
            <Dropdown.Item>
              <Link to={`${match.url}/reading`}>Reading</Link>
            </Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
        <Menu.Menu as="a" position="right">
          <Menu.Item as="a" header>
            <Icon name="log out" />
            <Link to="/login">Log Out</Link>
          </Menu.Item>
        </Menu.Menu>
      </Container>
    </Menu>
    <Route exact path={match.url} component={Dashboard} />
    <Route exact path={`${match.url}/posts`} component={ArticleList} />
    <Route path={`${match.url}/:topicId`} component={ToBeDone} />
  </Container>
);

const ToBeDone = () => (
  <div>
    <h3>Sorry, this func is to be done</h3>
  </div>
);

export default Layout;
