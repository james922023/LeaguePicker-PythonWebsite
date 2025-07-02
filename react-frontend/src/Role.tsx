import topIMG from './../public/images/Top_icon.png'
import botIMG from './../public/images/Bottom_icon.png'
import jungleIMG from './../public/images/Middle_icon.png'
import midIMG from './../public/images/Jungle_icon.png'
import supportIMG from './../public/images/Support_icon.png'

import './Role.css'

function Role () {
    return(
        <>
        <div id='roles-container'>
            <div id='role-container'>
                <p>Top</p>
                <img src={topIMG} id='role_images'></img>
            </div>
            <div id='role-container'>
                <p>Bot</p>
                <img src={botIMG} id='role_images'></img>
            </div>
            <div id='role-container'>
                <p>Mid</p>
                <img src={midIMG} id='role_images'></img>
            </div>
            <div id='role-container'>
                <p>Supp</p>
                <img src={supportIMG} id='role_images'></img>
            </div>
            <div id='role-container'>
                <p>Jg</p>
                <img src={jungleIMG} id='role_images'></img>
            </div>
        </div>
        </>
    )
}

export default Role