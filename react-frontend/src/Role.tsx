import Navbar from './Navbar';
import './Role.css'

import { Link } from 'react-router-dom';

function Role () {
    return(
        <>
        <Navbar/>
        <div id='role'>
            <div id='roles-container'>
                <div id='role-container'>
                    <Link to="/details" state={{role:'top'}}><img src='/images/Top_icon.png' id='role_images'></img></Link>
                </div>
                <div id='role-container'>
                    <Link to="/details" state={{role:'bot'}}><img src="/images/Bottom_icon.png" id='role_images'></img></Link>
                </div>
                <div id='role-container'>
                    <Link to="/details" state={{role:'mid'}}><img src="/images/Middle_icon.png" id='role_images'></img></Link>
                </div>
                <div id='role-container'>
                    <Link to="/details" state={{role:'support'}}><img src="/images/Support_icon.png" id='role_images'></img></Link>
                </div>
                <div id='role-container'>
                    <Link to="/details" state={{role:'jungle'}}><img src="/images/Jungle_icon.png" id='role_images'></img></Link>
                </div>
            </div>
            <p id='Choose_Role'>CHOOSE YOUR ROLE!</p>
        </div>
        </>
    )
}

export default Role