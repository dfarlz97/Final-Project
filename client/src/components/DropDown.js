import { React } from "react";
import { Link } from "react-router-dom";

export default function Dropdown() {
  return (
      <nav className = "Dropdown-Menu">
            <Link className="dropDownLink" to="/" exact="true">
            Home
            </Link>
            <Link className="dropDownLink" to="/appointments" exact="true">
            Appointments
            </Link>
            <Link className="dropDownLink" to="/signup" exact="true">
            Sign-up/Login
            </Link>
      </nav>
      );
    }
    