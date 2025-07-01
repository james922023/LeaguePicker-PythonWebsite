import './App.css'
import titleLogo from  './../public/images/ChampionPickerLogo.png'
import CharacterSelect from './CharacterSelect'

function App() {
  
  return (
    <>
    <body>
        <div id="title_section">
            <img src={titleLogo} alt="Logo"/>
        </div>
        <div id="horizontal_container">
            <div id="left_container">
              <CharacterSelect statueNumber={1}></CharacterSelect>
            </div>
            <div id="right_container">
              <CharacterSelect statueNumber={0}></CharacterSelect>
            </div>
        </div>
    </body>
    </>
  )
}

export default App
