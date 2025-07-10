import axios from "axios"
import { useEffect, useState} from "react"
import Navbar from './Navbar';

function Details(){

    const [topBuilds, setTopBuilds] = useState<TopBuild[]>([]);
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
        const buildURL = 'http://127.0.0.1:8000/api/topbuilds/';

        axios.get<TopBuild[]>(buildURL, { withCredentials: true })  // Include cookies/session
            .then(response => {
                setTopBuilds(response.data);
                setLoading(false);
            })
            .catch(error => {
                console.error("Error fetching top builds:", error);
                setLoading(false);
            });
    }, []);

    return(
        <>
        <Navbar/>
        <div className="details-page">
        {loading ? (
          <p>Loading...</p>
        ) : (
          topBuilds.map((build) => (
            <div key={build.id}>
              <img src={build.champion}></img>
              <p>Items:</p>
                <div className="item-images">
                  {build.items.map((itemUrl, idx) => (
                    <img key={idx} src={itemUrl} alt={`item-${idx}`} height={48} />
                  ))}
                </div>
              <p>Runes:</p>
                <div className="rune-images">
                  {build.runes.map((runeUrl, idx) => (
                    <img key={idx} src={runeUrl} alt={`rune-${idx}`} height={32} />
                  ))}
                </div>
              <p>Ability Order:</p>
              <ul>
                {Object.entries(build.ability_order)
                    .sort((a, b) => a[1] - b[1]) // sort by numeric value
                    .map(([ability, order]) => (
                    <li key={ability}>
                        {order}: {ability}
                    </li>
                    ))}
              </ul>
            </div>
          ))
        )}
        </div>
        </>
    )
}
export default Details