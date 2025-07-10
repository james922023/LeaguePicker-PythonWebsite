import React from 'react';

interface LeagueRune {
    name: string;
    url: string;
}

interface RuneSelectorProps {
    runes: LeagueRune[];
    selectedRunes: LeagueRune[]; 
    onItemClick: (rune: LeagueRune) => void;  
}

const RuneSelector: React.FC<RuneSelectorProps> = ({ runes, selectedRunes, onItemClick }) => {
    return (
        <div id="RuneGrid">
            {runes.map((rune) => (
                <div className="runeIcon" key={rune.name}>
                    <img
                        src={rune.url}
                        onClick={() => onItemClick(rune)} 
                        className={
                            selectedRunes.some(i => i.name === rune.name)
                                ? 'clicked'
                                : 'notClicked'
                        }
                        alt={rune.name}
                    />
                </div>
            ))}
        </div>
    );
};

export default RuneSelector;