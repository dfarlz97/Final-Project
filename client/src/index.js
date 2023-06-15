import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";
import "./index.css";
import App from "./Components/App.js"

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <App>
      </App>
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);