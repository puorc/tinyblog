import React from "react";
import { Query } from "react-apollo";
import gql from "graphql-tag";
import { Button, Checkbox, Icon, Table, Menu } from "semantic-ui-react";

const ArticlePostQuery = gql`
  {
    allArticles {
      edges {
        node {
          title
          author {
            username
          }
          category {
            name
          }
          comments {
            edges {
              node {
                author
              }
            }
          }
          createdTime
        }
      }
    }
  }
`;

class ArticleList extends React.Component {
  render() {
    return (
      <Query query={ArticlePostQuery}>
        {({ loading, error, data }) => {
          if (loading) return <div>Fetching</div>;
          if (error) return <div>rr</div>;
          return (
            <Table celled compact definition>
              <Table.Header fullWidth>
                <Table.Row>
                  <Table.HeaderCell />
                  <Table.HeaderCell width={6}>Title</Table.HeaderCell>
                  <Table.HeaderCell width={2}>Author</Table.HeaderCell>
                  <Table.HeaderCell width={2}>Categories</Table.HeaderCell>
                  <Table.HeaderCell width={2}>Tags</Table.HeaderCell>
                  <Table.HeaderCell width={1}>Comments</Table.HeaderCell>
                  <Table.HeaderCell width={2}>Dates</Table.HeaderCell>
                  <Table.HeaderCell width={1}>Operation</Table.HeaderCell>
                </Table.Row>
              </Table.Header>

              <Table.Body>
                {data.allArticles.edges.map(item => (
                  <Table.Row>
                    <Table.Cell collapsing>
                      <Checkbox />
                    </Table.Cell>
                    <Table.Cell>{item.node.title}</Table.Cell>
                    <Table.Cell>{item.node.author.username}</Table.Cell>
                    <Table.Cell>{item.node.category.name}</Table.Cell>
                    <Table.Cell>no tag</Table.Cell>
                    <Table.Cell>{item.node.comments.edges.length}</Table.Cell>
                    <Table.Cell>{item.node.createdTime}</Table.Cell>
                    <Table.Cell>
                      <Button.Group
                        buttons={[
                          { key: "edit", icon: "edit" },
                          { key: "trash", icon: "trash" },
                          { key: "eye", icon: "eye" }
                        ]}
                      />
                    </Table.Cell>
                  </Table.Row>
                ))}
              </Table.Body>
              <Table.Footer fullWidth>
                <Table.Row>
                  <Table.HeaderCell />
                  <Table.HeaderCell colSpan="16">
                    <Menu floated="right" pagination>
                      <Menu.Item as="a" icon>
                        <Icon name="chevron left" />
                      </Menu.Item>
                      <Menu.Item as="a">1</Menu.Item>
                      <Menu.Item as="a">2</Menu.Item>
                      <Menu.Item as="a">3</Menu.Item>
                      <Menu.Item as="a">4</Menu.Item>
                      <Menu.Item as="a" icon>
                        <Icon name="chevron right" />
                      </Menu.Item>
                    </Menu>
                  </Table.HeaderCell>
                </Table.Row>
              </Table.Footer>
            </Table>
          );
        }}
      </Query>
    );
  }
}

export default ArticleList;
