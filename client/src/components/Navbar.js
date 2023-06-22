import { React, useState } from "react";
import Dropdown from "./DropDown.js";
import * as RxIcons from "react-icons/rx";
export default function Navbar() {
  const [dropDown, setDropDown] = useState(false);

  const toggleDropDown = () => {
    setDropDown(!dropDown);
  };

  return (
    <>
      <header className="navbar">

        <h1 id="title">Skylark Neuropsychology</h1>
        <button className = "Dropdown-Button" onClick={toggleDropDown} id="dropdown-button">
          {<RxIcons.RxHamburgerMenu />}
        </button>
        
      </header>
      {dropDown ? <Dropdown /> : null}
    </>
  );
}