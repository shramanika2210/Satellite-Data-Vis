import React from 'react';
import './footer.css';
import logo from '../assets/log.png';
import Contact from './contact';


function Footer() {
  return (
        <footer class="footer-distributed">

			<div class="footer-left">
                <div style={{display:"flex"}}>
                <img src={logo} alt="Logo" className="logo" />
				<h3>Country<span>Side</span></h3>
                </div>
                

				<p class="footer-links">
					<a href="/" class="link-1">Home</a>
					
					<a href="/Monitor">Monitor</a>
				</p>

				<p class="footer-company-name">Afrah Mulla</p>
				<p class="footer-company-name">Zaara Shajal Ansari</p>
				<p class="footer-company-name">Shramanika Ghamre</p>
				<p class="footer-company-name">Farha Naaz Ansari</p>
			</div>

			<div class="footer-center">

			<p style={{ color: "white",  fontSize: "20px" }}>
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

			<div class="footer-right">

				{/* <p class="footer-company-about">
					<span>About the company</span>
					Lorem ipsum dolor sit amet, consectateur adispicing elit. Fusce euismod convallis velit, eu auctor lacus vehicula sit amet.
				</p>

				<div class="footer-icons">

					<a href="#"><i class="fa fa-facebook"></i></a>
					<a href="#"><i class="fa fa-twitter"></i></a>
					<a href="#"><i class="fa fa-linkedin"></i></a>
					<a href="#"><i class="fa fa-github"></i></a>

				</div> */}
                <Contact/>

			</div>

		</footer>
  )
}

export default Footer