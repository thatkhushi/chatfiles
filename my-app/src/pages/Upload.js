import React from "react";
import "./u.css";
import Sidebar from "./sidebar";
import Fileicon from "./group-58.png"
import  { useState } from "react";
import axios from "axios";

export const Upload = () => {

  const [file, setFile] = useState(null);

  const fileUpload = async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      if (response.ok) {
        // Upload successful!
      } else {
        // Upload failed!
      }
    } catch (error) {
      // Handle error
    }
  };

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    setFile(file);

    if (file) {
      await fileUpload(file);
    }
  };
  return (
    
    <div className="upload">
    
      <div className="div">
        <img className="frame" alt="Frame" src="frame-1364.png" />
        <div className="overlap">
          <div className="frame-2">
          <input type="text" name="send" placeholder="Send a message" />
            <img className="vector" alt="Vector" src="vector.svg" />
          </div>
        </div>
        <div className="overlap-group">
          <div  className="upload-file-max-size">
            {/* Upload file */}
            <input
 
type="file"
 
onChange={handleFileUpload} />
            <br />
            max size(500 mb)
          </div>
          
          <img className="group" alt="Group" src={Fileicon} />
        </div>
             </div>
    </div>
  );
};

export default Upload