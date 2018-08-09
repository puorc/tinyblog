import React from "react";
import { Header, Statistic } from "semantic-ui-react";

const Dashboard = () => (
  <div>
    <Header as="h2">
      <Header.Content>Dashboard</Header.Content>
    </Header>
    <Statistic.Group>
      <Statistic>
        <Statistic.Value>22</Statistic.Value>
        <Statistic.Label>Posts</Statistic.Label>
      </Statistic>
      <Statistic>
        <Statistic.Value>10</Statistic.Value>
        <Statistic.Label>Pages</Statistic.Label>
      </Statistic>
      <Statistic>
        <Statistic.Value>22000</Statistic.Value>
        <Statistic.Label>Comments</Statistic.Label>
      </Statistic>
      <Statistic>
        <Statistic.Value>2</Statistic.Value>
        <Statistic.Label>Users</Statistic.Label>
      </Statistic>
      <Statistic>
        <Statistic.Value>10</Statistic.Value>
        <Statistic.Label>Tags</Statistic.Label>
      </Statistic>
      <Statistic>
        <Statistic.Value>5</Statistic.Value>
        <Statistic.Label>Categories</Statistic.Label>
      </Statistic>
    </Statistic.Group>
  </div>
);

export default Dashboard;
