import statue_char from "./../public/images/PlaystyleStatue1.png"
import statue_char2 from "./../public/images/PlaystyleStatue2.png"
import './App.css'
import { Link } from 'react-router-dom';

function CharacterSelect ({statueNumber=0}) {

    return (
        <>
        <div id="char-select-box">
            
            <Link to="/roles"><img id='statue_style' src={statueNumber==1? statue_char:statue_char2}></img></Link>
            <p id='chooserText'>{statueNumber==1?"James's playstyle consists of easier to play characters for the most part. This was due to the fact that he onetricked gangplank and then they reworked him making him difficult. In order to get a break from sweating with the new gangplank barrels, he expanded his playstyle to new champtions, ones needing single digit IQ.":"Darius's playstyle consists of hard to play fast paced characters. This is due to him being a fast paced zoomer European who cant sit still for two seconds and needs more action. In order to get more action from his usual yasuo, he expanded his champions to other crackead champions with lots of outplay potential and skill expression."}</p>
            
        </div>
        </>
    )
}

export default CharacterSelect