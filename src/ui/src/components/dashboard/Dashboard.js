import React from "react";
import { Header, Statistic, Dimmer, Loader } from "semantic-ui-react";
import { Query } from "react-apollo";
import gql from "graphql-tag";

const StatisticQuery = gql`
  {
    allArticles {
      edges {
        node {
          title
        }
      }
    }
    allTags {
      edges {
        node {
          id
        }
      }
    }
    allCategories {
      edges {
        node {
          id
        }
      }
    }
    allTags {
      edges {
        node {
          id
        }
      }
    }
    allComments {
      edges {
        node {
          id
        }
      }
    }
  }
`;

class Dashboard extends React.Component {
  render() {
    return (
      <Query query={StatisticQuery}>
        {({ loading, error, data }) => {
          let content;
          if (loading) {
            content = (
              <Dimmer active>
                <Loader />
              </Dimmer>
            );
          } else if (error) {
            content = <div>Error!</div>;
          } else {
            content = (
              <Statistic.Group>
                <Statistic>
                  <Statistic.Value>
                    {data.allArticles.edges.length}
                  </Statistic.Value>
                  <Statistic.Label>Posts</Statistic.Label>
                </Statistic>
                <Statistic>
                  <Statistic.Value>
                    {data.allComments.edges.length}
                  </Statistic.Value>
                  <Statistic.Label>Comments</Statistic.Label>
                </Statistic>
                <Statistic>
                  <Statistic.Value>{data.allTags.edges.length}</Statistic.Value>
                  <Statistic.Label>Tags</Statistic.Label>
                </Statistic>
                <Statistic>
                  <Statistic.Value>
                    {data.allCategories.edges.length}
                  </Statistic.Value>
                  <Statistic.Label>Categories</Statistic.Label>
                </Statistic>
              </Statistic.Group>
            );
          }
          return (
            <div>
              <Header as="h2">
                <Header.Content>Dashboard</Header.Content>
              </Header>
              {content}
            </div>
          );
        }}
      </Query>
    );
  }
}

export default Dashboard;
