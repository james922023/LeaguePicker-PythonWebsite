import { useNavigate } from 'react-router-dom';

import './App.css'

import Navbar from './Navbar';

function App() {
  const navigate = useNavigate();
  const handleClick=()=>{
    navigate('/roles');
  };
  return (
    <>
    <Navbar/>
    <div className='TitleBox'>
        <div id='description-box'>
          <h2>What's up! Welcome to League Papi!</h2>
          <p>What is it?</p>
          <p>Im Glad You Asked!</p>
          <p>League Papi picks characters and builds for you so you dont have to think!</p>
          <p>No thinking! isnt that great!</p>
          <p>Are you ready for papi to take care of you?!</p>
        </div>
        <button className='button-13' onClick={handleClick}> YES &#128513;</button>
    </div>
    <div className='backgroundImageBox'>
    </div>
    </>
  )
}

export default App
