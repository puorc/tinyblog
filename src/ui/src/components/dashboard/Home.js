import React from "react";
import { Container } from "semantic-ui-react";
import Navbar from "./Navbar";
import All from "./All";

const Layout = () => (
  <Container style={{ marginTop: "80px", marginLeft: "90px" }}>
    <Navbar />
    <All />
  </Container>
);

export default Layout;
