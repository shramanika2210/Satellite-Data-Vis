import { React, useState } from "react";
import "./all.css";
import Grid from "@mui/material/Grid";
import Navbar from "./Navbar";
import Upload from "./upload";
import axios from "axios";

const Monitor = () => {
  const [Result, setresult] = useState(
    "Result will be shown here...:"
  );

  const handleImageUpload = async (imageData) => {
    const formData = new FormData();
    formData.append("file", imageData);
    // console.log("Base64-encoded image data:", formData);
    try {
      const res = await axios.post("http://127.0.0.1:5000/test", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
          // 'Access-Control-Allow-Origin': '*',
          // 'Access-Control-Allow-Methods': 'POST',
          // 'Access-Control-Allow-Headers': 'Content-Type'
        },
      });
      console.log(res);
      if (res.status == 200) {
        const text = await res.data;
        setresult(text);
        console.log("Image uploaded successfully", text);
      } else {
        console.error("Failed to upload image", res.data);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };
  const veg = Result.split(/\. |:/);
  const thcolo = veg[1]
  const theme = thcolo.split(" ")[1]

  return (
    <>
      <Navbar />

      <Grid container spacing={2}>
        <Grid item xs={8}>
          <Upload onImageUpload={handleImageUpload} />
        </Grid>
        <Grid item xs={4}>
          <div className="answerbox">
            <p>
              {veg.map((text) => {
                  return <p style={{color:theme ==="High" ? "green" : theme ==="Moderate" ? "blue": theme ==="Low" ? "red": "black"}}>{text}</p>;
              })}
            </p>
          </div>
        </Grid>
      </Grid>

    </>
  );
};

export default Monitor;
