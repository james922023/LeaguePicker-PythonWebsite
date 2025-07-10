import React from 'react';

interface LeagueChamp {
    name: string;
    url: string;
}

interface ChampSelectorProps {
    champs: LeagueChamp[];
    selectedChamp: LeagueChamp | null;
    onChampClick: (champ: LeagueChamp) => void;
}

const ChampSelector: React.FC<ChampSelectorProps> = ({ champs, selectedChamp, onChampClick }) => {
    return (
        <div id="champGrid">
            {champs.map((champ) => (
                <div className="champIcon" key={champ.name}>
                    <img
                        src={champ.url}
                        onClick={() => onChampClick(champ)} // ✅ Pass full object
                        className={selectedChamp?.name === champ.name ? 'clicked' : 'notClicked'}
                        alt={champ.name}
                    />
                </div>
            ))}
        </div>
    );
};

export default ChampSelector;