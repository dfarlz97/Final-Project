import React from "react";
import Navbar from "./Navbar.js";
import Home from "./Home.js";
import { Route, Routes } from "react-router-dom";
import Login from "./Login.js";
import Signup from "./Signup.js";
import LoginModal from "./LoginModal.js";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" exact="true" element={<LoginModal />} />
        <Route path="/Home" exact="true" element={<Home/>} />
        <Route path="/signup" exact="true" element={<Signup />} />
        <Route path="/login" exact="true" element={<Login />} />
      </Routes>
    </div>
  );
}

export default App;