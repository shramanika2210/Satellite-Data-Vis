import React from "react";
import "./all.css";
import { Link } from "react-router-dom";
import Pic from "../assets/farm.jpg";

const Box = () => {
  return (
    <div style={{ textAlign: "center", marginTop: "30px" }}>
      <div
        style={{
          width: "100vw",
          maxWidth: "82rem",
          height: "20rem",
          backgroundColor: "#0d7663",
          // backdropFilter: "blur(5px)",
          margin: "0 auto",
          display: "flex",
          boxshadow: "0px 2px 5px rgba(0, 0, 0, 0.851)",
        }}
      >
        <div style={{ textAlign: "center" }}>
          {/* Text content */}
          <h1 style={{ paddingTop: "20px", color: "white", fontSize: "40px" }}>
            Crop Monitoring
          </h1>
          <p style={{ color: "white", padding: "10px", fontSize: "20px" }}>
            In the ever-evolving landscape of agriculture, precision and
            efficiency are paramount. Farmers and agronomists face the ongoing
            challenge of maximizing yields while minimizing resource use and
            environmental impact. In response to this need, we proudly present
            our approach to it that provides a suggestion considering crop
            health issues that helps farmers to make better decisions for their
            crop.
          </p>
        </div>
        <div style={{}}>
          {/* Image content */}
          <img
            src={Pic}
            alt="farm"
            style={{ height: "20rem", objectFit: "contain" }}
          />
        </div>
      </div>

      <div
        style={{
          display: "flex",
          justifyContent: "space-around",
          marginTop: "40px",
        }}
      >
        {/* Two additional boxes */}
        <div
          style={{
            width: "35rem",
            height: "13rem",
            background: "#0d7663",
            textAlign: "center",
          }}
        >
          <h2 style={{ color: "white", fontSize: "35px" }}>We Provide</h2>
          <p style={{ color: "white" }}>A better Suggetion</p>
          <h5 style={{ color: "white", padding: "8px" }}>
            Our team make sure that you gain a better experiance with us and
            detect the crop health issue with its causes.
          </h5>
        </div>
        <div
          style={{
            width: "35rem",
            height: "13rem",
            background: "#0d7663",
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <p style={{ color: "white", fontSize: "30px" }}>
            Hit the start button and get benefitted by our suggestion
          </p>
          <Link to="/Monitor">
            <button
              style={{
                padding: "10px 20px",
                backgroundColor: "blue",
                color: "white",
                border: "none",
                borderRadius: "5px",
                cursor: "pointer",
              }}
            >
              START
            </button>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Box;
