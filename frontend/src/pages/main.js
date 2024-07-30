import React from 'react'
import Navbar from '../components/Navbar'
import Home from '../components/Home';
import Footer from '../components/Footer';

export default function main() {
  return (
   <>
   <Navbar />
   <Home />
   <div style={{marginTop:'40px'}}>
   <Footer />
   </div>
   
   </>

  )
}
