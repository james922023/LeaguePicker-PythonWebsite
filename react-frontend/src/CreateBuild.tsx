import axios from "axios"
import { useEffect, useState} from "react"
import './CreateBuild.css'
import Navbar from './Navbar';
import ChampSelector from './ChampSelector';
import ItemSelector from './ItemSelector';
import RuneSelector from "./RuneSelector";

function CreateBuild () {
    
    const [LeagueChamps, setLeagueChamps] = useState < LeagueChamp[] > ([])
    const [selectedChamp, setSelectedChamp] = useState<LeagueChamp | null>(null);

    const [LeagueItems, setLeagueItems] = useState <LeagueItem[]> ([])
    const [selectedItems, setSelectedItems] = useState<LeagueItem[]>([]);

    const [LeagueRunes, setLeagueRunes] = useState <LeagueRune[]> ([])
    const [selectedRunes, setSelectedRunes] = useState<LeagueRune[]>([]);

    const [selectedRole, setSelectedRole] = useState<string>('');

    interface LeagueChamp {
        name: string;
        url: string;
    }

    interface LeagueItem{
        name:string;
        url:string;
    }

    interface LeagueRune {
    name: string;
    url: string;
    }

    useEffect(()=>{
        const itemsURL='http://127.0.0.1:8000/get/items/'
        axios.get<LeagueItem[]>(itemsURL)
        .then(response => setLeagueItems(response.data))
    },[])

    useEffect(()=>{
        const champsURL='http://127.0.0.1:8000/get/champs/'
        axios.get<LeagueChamp[]>(champsURL)
        .then(response => setLeagueChamps(response.data))
    },[])

    useEffect(()=>{
        const runesURL='http://127.0.0.1:8000/get/runes/'
        axios.get<LeagueRune[]>(runesURL)
        .then(response => setLeagueRunes(response.data))
    },[])

    const handleChampClick = (champ: LeagueChamp) => {
        setSelectedChamp(prev =>
            prev?.name === champ.name ? null : champ
        );

        console.log("Selected Champion:", champ.name);
        console.log("Champion URL:", champ.url);
    };

    const handleItemClick = (item: LeagueItem) => {
        setSelectedItems(prev => {
            const isSelected = prev.some(i => i.name === item.name);
            const updated = isSelected
                ? prev.filter(i => i.name !== item.name)
                : [...prev, item];

            console.log("Selected Items:", updated); 

            return updated;
        });
    };

    const handleRuneClick = (item: LeagueRune) => {
        setSelectedRunes(prev => {
            const isSelected = prev.some(i => i.name === item.name);
            const updated = isSelected
                ? prev.filter(i => i.name !== item.name)
                : [...prev, item];

            console.log("Selected Runes:", updated); 

            return updated;
        });
    };

    const handleSubmit = () => {
        if (!selectedChamp) {
            alert("Please select a champion.");
            return;
        }

        const abilityOrder = {
            Q: Number((document.getElementById('Qorder') as HTMLInputElement).value),
            W: Number((document.getElementById('Worder') as HTMLInputElement).value),
            E: Number((document.getElementById('Eorder') as HTMLInputElement).value)
        };

        const postData = {
            champion: selectedChamp.url,
            items: selectedItems.map(item => item.url),
            runes: selectedRunes.map(rune => rune.url),
            ability_order: abilityOrder
        };

        const postUrl = `http://127.0.0.1:8000/api/${selectedRole.toLowerCase()}builds/`;

        axios.post(postUrl, postData, {
            withCredentials: true,
            headers:{
                'X-CSRFToken': getCookie('csrftoken') || ''
            }
        })
        .then(response => {
            console.log("Build submitted successfully:", response.data);
            alert("Build submitted successfully!");
        })
        .catch(error => {
            console.error("Error submitting build:", error);
            alert("Failed to submit build.");
        });
        };

        function getCookie(name: string): string | null {
            const cookieValue = document.cookie
                .split('; ')
                .find(row => row.startsWith(name + '='));
            return cookieValue ? decodeURIComponent(cookieValue.split('=')[1]) : null;
        }

    return (
        <>
        <Navbar/>
        <div id='add_build'>
            <p style={{color:'white',fontSize:'2vmin',margin:'0'}}>Champions:</p>
            <ChampSelector
                    champs={LeagueChamps}
                    selectedChamp={selectedChamp}
                    onChampClick={handleChampClick}
                />
            <p style={{color:'white',fontSize:'2vmin',margin:'0'}}>Items:</p>
            <ItemSelector
                    items={LeagueItems}
                    selectedItems={selectedItems}
                    onItemClick={handleItemClick}
                />
            <p style={{color:'white',fontSize:'2vmin',margin:'0'}}>Abilites Order:</p>
            <ul className='abilityOrder'>
                <li><img src='/images/Q.png'></img> <input id='Qorder' type="number" max="3" min='0'/> </li>
                <li><img src='/images/W.png'></img><input id='Worder' type="number" max="3" min='0'/></li>
                <li><img src='/images/E.png'></img><input id='Eorder' type="number" max="3" min='0'/></li>
            </ul>
            <p style={{color:'white',fontSize:'2vmin',margin:'0'}}>Runes:</p>
            <RuneSelector
                    runes={LeagueRunes}
                    selectedRunes={selectedRunes}
                    onItemClick={handleRuneClick}
                />
            <div className="role-selector">
                <p>Select Role:</p>
                {['Top', 'Mid', 'Jungle', 'Support', 'Bot'].map(role => (
                    <label key={role}>
                    <input
                        type="radio"
                        value={role}
                        checked={selectedRole === role}
                        onChange={(e) => setSelectedRole(e.target.value)}
                        name="role"
                    />
                    {role}
                    </label>
                ))}
            </div>
            <button className="submit_button" onClick={handleSubmit}>ADD BUILD!</button>
        </div>
        </>
    )
}

export default CreateBuild 