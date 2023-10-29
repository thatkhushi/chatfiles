
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
// import { Route , Switch} from "react-router-dom";

import Home from "./pages/Home";
import SignUp from "./pages/SignUp";
import Login from "./pages/Login";
import Upload from "./pages/Upload";


export default function App() {
  return (
    <div>
    <BrowserRouter>
      <Routes>
        
          <Route index element={<Home />} />
          <Route path="/Home" element={<Home />} />
          <Route path="/SignUp" element={<SignUp />} />
          <Route path="/Login" element={<Login />} />
          <Route path="/Upload" element={<Upload />} />
        
      </Routes>
    </BrowserRouter>
    </div>
  );
}