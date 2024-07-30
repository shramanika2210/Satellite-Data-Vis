import React from "react";
import "./all.css"; // Import your CSS file for styling
import Pic from "../assets/side.jpg";

const About = () => {
  

  return (
    <div
      // className="container"
      id="about"
      style={{
        backgroundColor: "#3bb19b",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "50vh",
        width: "98.9vw",
        position: "relative",
      }}
      
    >
        <img
          src={Pic}
          alt="side"
          style={{ height: "100%", width: "30rem" }}
        />
      <div className="left-side">
        {/* Animation with text */}
        <p style={{ color: "white", paddingLeft: "30px", fontSize: "20px" , width:"40rem"}}>
          Welcome to our website! At the heart of our digital presence lies a
          vital link to our audience – our Contact Page. Here, we invite you to
          connect with us, share your thoughts, inquiries.
          <br/>
          <br/>
          Our Contact Page isn't just a means of communication; it's a gateway to building
          lasting relationships with our audience. So, whether you have a
          question, a suggestion, or just want to connect, we encourage you to
          reach out through our Contact Page. We look forward to hearing from
          you!
        </p>
      </div>
    </div>
  );
};

export default About;
