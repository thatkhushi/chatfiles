import * as React from "react";
import './SignUp.css';
import { Link } from 'react-router-dom';

function SignUp(props) {
    return (

        <div className="div">
            <div className="div-2">
                <div className="div-3">
                    <h4>Welcome to</h4>
                    <div className="div-4">Chatfiles.ai</div>
                </div>

                <div >
                    <form>


                        <input type="text" name="name" placeholder="Name" />
                        <input type="text" name="name" placeholder="Email Id/Phone" />
                        <input type="text" name="name" placeholder="Password" />
                        <input type="text" name="name" placeholder="Confirm Password" />


                    </form>
                </div>
               
                <div className="div-9">
                    <Link to ="" className="div-10">Sign Up</Link>
                </div>
                <div className="div-11">
                    <div className="div-12" />
                    <div className="div-13">OR</div>
                    <div className="div-14" />
                </div>
                <div className="div-15">
                    <img
                        loading="lazy"
                        src="https://cdn.builder.io/api/v1/image/assets/TEMP/25f215ec-de07-4022-89de-ab44a1555c87?"
                        className="img"
                    />
                    <img
                        loading="lazy"
                        src="https://cdn.builder.io/api/v1/image/assets/TEMP/07b0bb06-4dcf-43e5-bc1c-ce715d61039d?"
                        className="img-2"
                    />
                    <img
                        loading="lazy"
                        src="https://cdn.builder.io/api/v1/image/assets/TEMP/4f6bc85c-2b3d-47a4-9bd8-d003cb148ac9?"
                        className="img-3"
                    />
                </div>
                <div className="div-16">
                    <span >
                        Already have an account? <Link to="/Login" >Log In </Link>

                    </span>

                </div>
            </div>
        </div>

    );
}

export default SignUp;
