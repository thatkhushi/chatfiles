
import './Login.css';
import { Link } from 'react-router-dom';


function Login(props) {
    return (

        <div className="div">
            <div className="div-2">
                <div className="div-3">
                    <h4>Welcome to</h4>
                    <div className="div-4">Chatfiles.ai</div>
                </div>
                </div>

                <div class="social-button">
                    <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/25f215ec-de07-4022-89de-ab44a1555c87?" alt="Google Icon" class="icon"></img>
                       <span class="texts">Sign Up with Google</span>
                </div>

                <div class="social-button">
                    <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/07b0bb06-4dcf-43e5-bc1c-ce715d61039d?" alt="FB icon" class="icon"></img>
                       <span class="texts">Sign Up with Facebook</span>
                </div>

                <div className="div-11">
                    <hr></hr>
                    <div className="div-13">OR</div>
                   <hr></hr>
                </div>

                <div className='email' >
                    <form>


                        
                        <input type="text" name="name" placeholder="Email Id/Phone" />
                        <input type="text" name="name" placeholder="Password" />
                        


                    </form>
                </div>

                <div className="div9">
                    <a href="#" className="div-10">Login </a>
                </div>




                <div className="div-16">
                    <span >
                        Don't have an account? <Link to ="/SignUp" >Sign In</Link>

                    </span>

                </div>



                

                {/* <div className="login-with-google">
        <button className="login-with-google-child" />
        <div className="search-1-parent">
          <img className="search-1-icon" alt="" src="/search-1.svg" />
          <div className="login-with-google1">Login with Google</div>
        </div>
      </div>
      <div className="login-with-facebook">
        <button className="login-with-google-child" />
        <div className="login-with-facebook-parent">
          <div className="login-with-facebook1">Login with Facebook</div>
          <img className="vector-icon" alt="" src="/vector.svg" />
        </div>
      </div>

                

                     <div className="div-11">
                    <div className="div-12" />
                    <div className="div-13">OR</div>
                    <div className="div-14" />
                </div>

                <div >
                    <form>


                        
                        <input type="text" name="name" placeholder="Email Id/Phone" />
                        <input type="text" name="name" placeholder="Password" />
                        


                    </form>

                    
                </div> */}



                </div>);
                }

                export default Login;