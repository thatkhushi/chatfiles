import './Home.css';
import "bootstrap/dist/css/bootstrap.min.css"
import SignUp from './SignUp';
import React, { useState } from 'react';
import { Link } from 'react-router-dom';


const Home=() => {

  

  return (
    <div className="App">
      
      <nav class="navbar">
		<div class="navdiv">
			<div class="logo"><a href="#">Chatfiles.ai</a> </div>
			<ul>
      <div className="list">
				<li><a href="#">Home</a></li>
				<li><a href="#">Documentation</a></li>
				<li><a href="#">Api reference</a></li>
        <li><a href="#">History</a></li></div>
        <div className="login">
				<button><Link to ="/Login">LogIn</Link></button>
        
				<button className="signup"  ><Link to ="/SignUp">SignUp</Link></button>
        

        </div>
			</ul>
		</div>
	</nav>


<div className="title">
<h1>Introducing Chatfiles.ai</h1></div>
    
    <div className="para"><p>An application designed to simplify the way you interact with PDF documents. With this innovative tool, you can effortlessly input your PDF files and receive invaluable insights and concise notes derived from their content.</p></div>
    
    <div class="button-container">
  <button class="button" >Get Started</button>
</div>


    <div class="flex-container">
    <div class="gradient-div">
  <p class="text"><b>Quickstart tutorial</b></p>
  <p class="text2">Get started with a quick tour.</p>
</div>
<div class="gradient-div2">
  <p class="text"><b>Quickstart tutorial</b></p>
  <p class="text2">Get started with a quick tour.</p>
</div>
</div>


    
    
    </div>


  );
}

export default Home;
