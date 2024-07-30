import React from 'react';
import { Link } from 'react-router-dom';
import './all.css';
import logo from '../assets/log.png';

const Navbar = () => {
  const user = localStorage.getItem("token");

  const handleLogout = () => {
		localStorage.removeItem("token");
		window.location.reload();
	};
  return (
    <div>
      <nav className="navbar">
        <div className="container">
          <a href="/" className="logo-container">
            <img src={logo} alt="Logo" className="logo" />
            <h1 className="site-name">COUNTRYSIDE</h1>
          </a>
          <div className="nav-links">
           
          
            {user?
            <li><div onClick={handleLogout} style={{cursor:"pointer"}}>logout</div></li>:
            <li><Link to="/login">Login</Link></li>}
          </div>
        </div>
      </nav>
    </div>
  );
};

export default Navbar; // Export Navbar as default
