import React, { useState } from 'react';
import "./all.css";

const UploadImageForm = ({ onImageUpload }) => {
  const [image, setImage] = useState(null);
  const [name, setname] = useState()

  const handleImageChange = (e) => {
    setImage(e.target.files[0]);
    setname(e.target.files[0].name)
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (image) {
      // Pass the base64-encoded image data to the parent component
      onImageUpload(image);
    }
  };

  return (
    <form onSubmit={handleSubmit} className='form-container'>
     
              <div class="upload-files-container">
                <div class="drag-file-area">
                  <span class="material-icons-outlined upload-icon">
                    {" "}
                    Image_upload{" "}
                  </span>
                  <h3 class="dynamic-message"> Drag & drop crop image </h3>
                  <label class="label">
                    {" "}
                    or{" "}
                    <span class="browse-files">
                      {" "}
                      <input
                        type="file"
                        class="default-file-input"
                        onChange={handleImageChange}
                        accept="image/*"
                      />{" "}
                      <span class="browse-files-text">browse file</span>{" "}
                      <span>from device</span>{" "}
                    </span>{" "}
                  </label>
                </div>
                <span class="cannot-upload-message">
                  {" "}
                  <span class="material-icons-outlined">error</span> Please
                  select a file first{" "}
                  <span class="material-icons-outlined cancel-alert-button">
                    cancel
                  </span>{" "}
                </span>
                <div class="file-block">
                  <div class="file-info">
                    {" "}
                    <span class="material-icons-outlined file-icon">
                      description
                    </span>{" "}
                    <span class="file-name"> </span> |{" "}
                    <span class="file-size"> </span>{" "}
                  </div>
                  <span class="material-icons remove-file-icon">delete</span>
                  <div class="progress-bar"> </div>
                </div>
                <p>{name}</p>
                <button type="submit" class="upload-button">
                  {" "}
                  Upload
                </button>
              </div>
    </form>
  );
};

export default UploadImageForm;
