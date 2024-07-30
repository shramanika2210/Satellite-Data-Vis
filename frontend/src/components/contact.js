import React, { useState, useRef } from "react";
import Toast from "./toast";
import emailjs from "@emailjs/browser";


const contact = () => {
  const [toastActive, setToastActive] = useState(false);
  const timer1 = useRef(null);

  const [control, setControl] = useState({
    name: "",
    email: "",
    mesg: "",
  });

  const form = useRef();
  const handlecontact = (e) => {
    e.preventDefault();

    emailjs
      .sendForm(
        "service_2u7t8e8",
        "template_mhl3rca",
        form.current,
        "barPhNUgA_B68Tggi"
      )
      .then(
        (result) => {
          console.log(result.text);
        },
        (error) => {
          console.log(error.text);
        }
      );

    setToastActive(true);

    timer1.current = setTimeout(() => {
      setToastActive(false);
    }, 5000);

    setControl({ name: "", email: "", mesg: "" });
  };
  return (
    <form ref={form} onSubmit={handlecontact}>
      <div>
        {/* Contact information text boxes */}
        <h1 style={{ color: "white" }}>Contact</h1>
        <div className="contact-info">
          <input
            type="text"
            placeholder="Name"
            name="pname"
            value={control.name}
            onChange={setControl}
            style={inputStyle}
            required
          />
          <input
            type="email"
            placeholder="Email"
            name="email"
            value={control.email}
            onChange={setControl}
            style={inputStyle}
            required
          />
          <textarea
            placeholder="Message"
            name="mesg"
            value={control.mesg}
            onChange={setControl}
            style={textareaStyle}
            required
          ></textarea>
          <button type="submit" style={buttonStyle}>
            SEND
          </button>
        </div>
      </div>
      {toastActive && <Toast />}
    </form>
  );
};

// Styles
const inputStyle = {
  width: "100%",
  padding: "10px",
  marginBottom: "15px",
  borderRadius: "5px",
  border: "1px solid #ccc",
  boxSizing: "border-box",
};

const textareaStyle = {
  width: "100%",
  padding: "10px",
  marginBottom: "15px",
  borderRadius: "5px",
  border: "1px solid #ccc",
  boxSizing: "border-box",
};

const buttonStyle = {
  marginTop: "10px",
  padding: "10px 20px",
  backgroundColor: "blue",
  color: "white",
  border: "none",
  borderRadius: "5px",
  cursor: "pointer",
};

export default contact;
