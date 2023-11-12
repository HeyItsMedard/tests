import React from "react";

const headerStyle = {
  backgroundColor: "#333",
  color: "#fff",
  padding: "20px",
  textAlign: "center",
};

const h1Style = {
  fontSize: "24px",
  margin: "0",
};

const Header = () => {
  return (
    <header style={headerStyle}>
      <h1 style={h1Style}>Todo App</h1>
    </header>
  );
};

export default Header;