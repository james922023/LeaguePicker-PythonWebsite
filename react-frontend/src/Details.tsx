import axios from "axios"
import { useEffect, useState} from "react"
import Navbar from './Navbar';
import './Details.css'
import { useLocation } from "react-router-dom";

function Details(){

    const location = useLocation();
    const role = location.state?.role;

    const [topBuild, setTopBuild] = useState<TopBuild | null>(null);
    const [loading, setLoading] = useState(true);

    interface TopBuild {
        id: number;
        champion: string;
        items: string[];
        runes: string[];
        ability_order: {
            Q: number;
            W: number;
            E: number;
        };
    }

    

    useEffect(() => {
        const buildURL = `http://127.0.0.1:8000/api/${role}builds/random/`;

        axios.get<TopBuild>(buildURL, { withCredentials: true })
            .then(response => {
              setTopBuild(response.data);
              setLoading(false);
            })
            .catch(error => {
                console.error(`Error fetching ${role} builds:`, error);
                setLoading(false);
            });
    }, []);

    return(
        <>
        <Navbar/>
        <div id='Detail-Background'>
        <div className="details-page">
        {loading ? (
          <p>Loading...</p>
        ) : topBuild ? (
          <div key={topBuild.id}>
            <img src={topBuild.champion} alt="Champion" />
            <p>Items:</p>
            <div className="item-images">
              {topBuild.items.map((itemUrl, idx) => (
                <img key={idx} src={itemUrl} alt={`item-${idx}`} height={48} />
              ))}
            </div>
            <p>Runes:</p>
            <div className="rune-images">
              {topBuild.runes.map((runeUrl, idx) => (
                <img key={idx} src={runeUrl} alt={`rune-${idx}`} height={32} />
              ))}
            </div>
            <p>Ability Order:</p>
            <ol className="abilityList">
              {Object.entries(topBuild.ability_order)
                .sort((a, b) => a[1] - b[1]) 
                .map(([ability]) => (
                  <li key={ability}>
                    <img src={`/images/${ability}.png`} alt={ability} />
                  </li>
                ))}
            </ol>
          </div>
        ) : (
          <p>No build found.</p>
        )}
        </div>
        </div>
        </>
    )
}
export default Details