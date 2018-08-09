import React from "react";
import {
  Container,
  Header,
  Grid,
  Segment,
  List,
  Dimmer,
  Loader
} from "semantic-ui-react";
import { Query } from "react-apollo";
import gql from "graphql-tag";
import Head from "./Head";
import Articles from "./Articles";
import Categories from "./Categories";
import Tags from "./Tags";

const QUERY = gql`
  {
    allArticles {
      edges {
        node {
          id
          title
          author {
            username
          }
          category {
            name
          }
          tags {
            edges {
              node {
                id
                name
              }
            }
          }
          createdTime
        }
      }
    }
    allCategories {
      edges {
        node {
          id
          name
        }
      }
    }
    allTags {
      edges {
        node {
          id
          name
        }
      }
    }
  }
`;

class Page extends React.Component {
  render() {
    return (
      <Query query={QUERY}>
        {({ loading, error, data }) => {
            console.log(data)
          if (loading)
            return (
              <Dimmer active>
                <Loader />
              </Dimmer>
            );
          else if (error) {
            console.log(error);
            return <div>Error!</div>;
          } else {
            return (
              <Container>
                <Head />
                <Grid columns="equal">
                  <Grid.Row>
                    <Grid.Column width={8}>
                      <Articles data={data.allArticles.edges} />
                    </Grid.Column>
                    <Grid.Column width={4}>
                      <Categories data={data.allCategories.edges} />
                      <Tags data={data.allTags.edges} />
                    </Grid.Column>
                  </Grid.Row>
                </Grid>
              </Container>
            );
          }
        }}
      </Query>
    );
  }
}

export default Page;
