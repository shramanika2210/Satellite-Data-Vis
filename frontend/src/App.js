// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Login from './components/Login/index';
import Register from './components/Singup/index';
import Main from './pages/main';
import Monitor from './components/Monitor';
// import About from './components/About';

function App() {
  const user = localStorage.getItem("token");

  return (
    <Router>
      <Routes>
        {user &&
         <> <Route path="/" exact element={<Main />} />
          {/* <Route path="/about" element={<About/>} /> */}
          <Route path="/monitor" element={<Monitor />} />
        </>
        } 
        <Route path="/" element={<Navigate replace to="/login" />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Register />} />
          {/* <Route path="/about" element={<About/>} /> */}
          <Route path="/monitor" element={<Navigate replace to="/login" />} />
        {/* Add other routes for Home, About, and Contact */}
      </Routes>
    </Router>
  );
}

export default App;
